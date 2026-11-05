"""Учебный read-only JSON API: файл данных не зависит от текущего каталога."""
import json
from pathlib import Path
from flask import Flask, jsonify, abort


def create_app():
    app = Flask(__name__)
    data_path = Path(__file__).resolve().parent.parent / "users.json"
    raw_users = json.loads(data_path.read_text(encoding="utf-8"))
    users = {key: {field: data[field] for field in ("name", "description")}
             for key, data in sorted(raw_users.items())}

    @app.get("/")
    def index():
        return jsonify(resources={"users": "/users", "user": "/users/<username>"},
                       current_uri="/")

    @app.get("/users")
    def all_users():
        return jsonify(users)

    @app.get("/users/<username>")
    def user_data(username):
        if username not in users:
            abort(404)
        return jsonify(users[username])

    @app.get("/users/<username>/something")
    def user_something(username):
        # Не реализованный endpoint отвечает контролируемым статусом, не traceback.
        abort(501)

    return app


app = create_app()
create_test_app = create_app

if __name__ == "__main__":
    app.run(port=5000)
