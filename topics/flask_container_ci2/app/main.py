"""Учебный API матриц: строки разделены n, индексы для пользователя с единицы."""
from flask import Flask, jsonify, abort, Response


def parse_matrix(value):
    if len(value) > 4096:
        abort(400, description="matrix is too large")
    rows = value.split("n")
    if (not rows or not rows[0] or any(len(row) != len(rows[0]) for row in rows)
            or any(ch not in "0123456789" for row in rows for ch in row)):
        abort(400, description="use equally sized digit rows separated by n")
    return rows


def create_app():
    app = Flask(__name__)

    @app.get("/")
    def index():
        return jsonify(resources={"matrix": "/matrix/<matrix>",
                                  "column": "/columns/<matrix>/<column_number>",
                                  "row": "/rows/<matrix>/<row_number>"},
                       current_uri="/", example="/matrix/123n456n789")

    @app.get("/matrix/<matrix>")
    def matrix_data(matrix):
        rows = parse_matrix(matrix)
        return Response(chr(10).join(" ".join(row) for row in rows),
                        mimetype="text/plain")

    @app.get("/columns/<matrix>/<int:column_number>")
    def column(matrix, column_number):
        rows = parse_matrix(matrix)
        if not 1 <= column_number <= len(rows[0]):
            abort(400, description="column out of range")
        return Response(chr(10).join(row[column_number - 1] for row in rows),
                        mimetype="text/plain")

    @app.get("/rows/<matrix>/<int:row_number>")
    def row(matrix, row_number):
        rows = parse_matrix(matrix)
        if not 1 <= row_number <= len(rows):
            abort(400, description="row out of range")
        return Response(" ".join(rows[row_number - 1]), mimetype="text/plain")

    return app


app = create_app()

if __name__ == "__main__":
    app.run(port=5000)
