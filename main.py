from flask import Flask, request, jsonify
from flask_restful import Api
import sqlite3

app = Flask(__name__)
api = Api(app)


def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("tabu.db")
    except sqlite3.error as e:
        print(e)
    return conn


@app.route("/tabuquestions", methods=["GET", "POST"])
def getQuestions():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM tabu")
        questions = [
            dict(id=row[0], answer=row[1], tip1=row[2], tip2=row[3], tip3=row[4], tip4=row[5], tip5=row[6])
            for row in cursor.fetchall()
        ]
        if questions is not None:
            return jsonify(questions)


if __name__ == "__main__":
    app.run(debug=True, threaded=True, use_reloader=False)
