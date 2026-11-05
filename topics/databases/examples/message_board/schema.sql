-- SQLite >= 3.37. foreign_keys must be enabled for EACH connection.
PRAGMA foreign_keys = ON;

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    display_name TEXT NOT NULL CHECK(length(trim(display_name)) > 0),
    contact_email TEXT
) STRICT;
CREATE TABLE boards (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(trim(name)) > 0)
) STRICT;
CREATE TABLE board_members (
    board_id INTEGER NOT NULL REFERENCES boards(id) ON DELETE RESTRICT,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE RESTRICT,
    active INTEGER NOT NULL DEFAULT 1 CHECK(active IN (0, 1)),
    PRIMARY KEY(board_id, user_id)
) STRICT;
CREATE INDEX board_members_by_user ON board_members(user_id, board_id);

CREATE TABLE messages (
    id INTEGER PRIMARY KEY,
    board_id INTEGER NOT NULL,
    author_id INTEGER NOT NULL,
    reply_to_id INTEGER,
    body TEXT NOT NULL CHECK(length(trim(body)) > 0),
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    UNIQUE(id, board_id),
    CHECK(reply_to_id IS NULL OR reply_to_id <> id),
    FOREIGN KEY(board_id, author_id) REFERENCES board_members(board_id, user_id),
    FOREIGN KEY(reply_to_id, board_id) REFERENCES messages(id, board_id) ON DELETE RESTRICT
) STRICT;
CREATE INDEX messages_feed ON messages(board_id, created_at, id);
CREATE INDEX messages_by_author ON messages(board_id, author_id);
CREATE INDEX messages_by_parent ON messages(reply_to_id, board_id);
-- Parent and board are immutable. Together with immediate FKs and no self-reference,
-- this prevents a cycle introduced by moving existing messages into another thread.
CREATE TRIGGER messages_immutable_thread
BEFORE UPDATE OF reply_to_id, board_id ON messages
WHEN NEW.reply_to_id IS NOT OLD.reply_to_id OR NEW.board_id <> OLD.board_id
BEGIN
    SELECT RAISE(ABORT, 'thread parent and board are immutable');
END;

CREATE TABLE categories (
    id INTEGER PRIMARY KEY,
    board_id INTEGER NOT NULL REFERENCES boards(id) ON DELETE RESTRICT,
    name TEXT NOT NULL CHECK(length(trim(name)) > 0),
    UNIQUE(board_id, name),
    UNIQUE(id, board_id)
) STRICT;
CREATE TABLE message_categories (
    message_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    board_id INTEGER NOT NULL,
    PRIMARY KEY(message_id, category_id),
    FOREIGN KEY(message_id, board_id) REFERENCES messages(id, board_id) ON DELETE RESTRICT,
    FOREIGN KEY(category_id, board_id) REFERENCES categories(id, board_id) ON DELETE RESTRICT
) STRICT;
CREATE INDEX message_categories_by_category ON message_categories(category_id, board_id);
CREATE TABLE message_mentions (
    message_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    board_id INTEGER NOT NULL,
    PRIMARY KEY(message_id, user_id),
    FOREIGN KEY(message_id, board_id) REFERENCES messages(id, board_id) ON DELETE RESTRICT,
    FOREIGN KEY(board_id, user_id) REFERENCES board_members(board_id, user_id) ON DELETE RESTRICT
) STRICT;
CREATE INDEX message_mentions_by_user ON message_mentions(board_id, user_id);
CREATE TABLE message_views (
    message_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    board_id INTEGER NOT NULL,
    viewed_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    PRIMARY KEY(message_id, user_id, viewed_at),
    FOREIGN KEY(message_id, board_id) REFERENCES messages(id, board_id) ON DELETE RESTRICT,
    FOREIGN KEY(board_id, user_id) REFERENCES board_members(board_id, user_id) ON DELETE RESTRICT
) STRICT;
CREATE INDEX message_views_by_user ON message_views(board_id, user_id);
