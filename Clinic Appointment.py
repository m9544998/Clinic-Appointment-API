
from flask import Flask, request, jsonify
import sqlite3
app = Flask(__name__)

DATABASE = "clinic.db"


def get_db():

    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    return conn


def init_db():

    conn = get_db()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS appointments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_name TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


init_db()


# Book Appointment
@app.route("/appointments", methods=["POST"])
def add_appointment():

    data = request.get_json()

    if not data or not data.get("patient_name"):

        return jsonify({
            "error": "patient_name required"
        }), 400

    try:

        conn = get_db()

        conn.execute(
            """
            INSERT INTO appointments(
            patient_name
            )
            VALUES(?)
            """,
            (data["patient_name"],)
        )

        conn.commit()

        conn.close()

        return jsonify({
            "message":
            "Appointment booked"
        }), 201


    except sqlite3.Error as e:

        return jsonify({
            "error":
            str(e)
        }), 500


# View Appointments
@app.route("/appointments", methods=["GET"])
def get_appointments():

    conn = get_db()

    rows = conn.execute(
        "SELECT * FROM appointments"
    ).fetchall()

    conn.close()

    return jsonify([
        dict(row)
        for row in rows
    ])


# Delete Appointment
@app.route("/appointments/<int:id>", methods=["DELETE"])
def delete_appointment(id):

    conn = get_db()

    conn.execute(
        """
        DELETE FROM appointments
        WHERE id=?
        """,
        (id,)
    )

    conn.commit()

    conn.close()

    return jsonify({
        "message":
        "Appointment deleted"
    })
if __name__ == "__main__":
    app.run(debug=True)