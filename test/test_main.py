from fastapi.testclient import TestClient
from main import app  # Import your FastAPI app

client = TestClient(app)

def test_obtener_alumnos():
    response = client.get("/alumnos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Check if the response is a list

def test_agregar_alumno():
    nuevo_alumno = {
        "nombre": "Juan",
        "apellidos": "Pérez",
        "carrera": "Ingeniería",
        "facultad": "Facultad de Ingeniería"
    }
    response = client.post("/alumnos/", json=nuevo_alumno)
    assert response.status_code == 200
    assert response.json() == nuevo_alumno  # Check if the returned data matches

def test_eliminar_alumno():
    response = client.delete("/alumnos/Juan")
    assert response.status_code == 200
    assert response.json()["nombre"] == "Juan"  # Check if the deleted student is returned