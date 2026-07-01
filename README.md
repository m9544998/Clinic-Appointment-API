# Clinic-Appointment-API
# Clinic Appointment API

A simple RESTful API built using Flask and SQLite to manage clinic appointments.

## Features

* Book Appointment
* View Appointments
* Delete Appointment
* Input Validation
* JSON Responses

---

## Technologies

* Python
* Flask
* SQLite3
* REST API

---

## Project Structure

```text
clinic-appointment-api/
│
├── app.py
├── clinic.db
├── README.md
└── requirements.txt
```

---

## Installation


Install Flask:

```bash
pip install flask
```

Run project:

```bash
python app.py
```

Server:

```text
http://127.0.0.1:5000
```

## API Endpoints

| Method | Endpoint           |
| ------ | ------------------ |
| POST   | /appointments      |
| GET    | /appointments      |
| DELETE | /appointments/<id> |

---

## Example Request

```json
{
 "patient_name":"Maheen"
}
```

Response:

```json
{
 "message":"Appointment booked"
}
```

---
## Author

Maheen Asad
