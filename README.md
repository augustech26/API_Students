# API_Students
API designed and developed as a demonstration project for the pre-specialization program at Dr. Andrés Bello University, built using Python (FastAPI).

Run the API: To run the API, use Uvicorn from the terminal.

```
uvicorn main:app --reload
```

This will start the server at http://127.0.0.1:8000.

Test the API: You can test the API using tools like Postman or cURL. You can also access the automatically generated documentation by FastAPI at http://127.0.0.1:8000/docs.

Create a student (POST):

URL: http://127.0.0.1:8000/alumnos/
Body (JSON):

```
{
    "nombre": "Juan",
    "apellidos": "Pérez",
    "carrera": "Ingeniería",
    "facultad": "Facultad de Ingeniería"
}
```

Get all students (GET):

URL: http://127.0.0.1:8000/alumnos/
Get a specific student (GET):

URL: http://127.0.0.1:8000/alumnos/0 (where 0 is the index of the student in the list).
