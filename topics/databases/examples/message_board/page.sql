-- SQLite parameters: board_id, cursor_created_at, cursor_id, limit.
SELECT id, created_at, body
FROM messages
WHERE board_id = ?
  AND (created_at, id) < (?, ?)
ORDER BY created_at DESC, id DESC
LIMIT ?;
