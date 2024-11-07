from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
from typing import List

app = FastAPI()

# Modelo de datos para un alumno
class Alumno(BaseModel):
    nombre: str
    apellidos: str
    carrera: str
    facultad: str

# Funciones para manejar la lectura y escritura del archivo JSON
def leer_alumnos():
    with open('alumnos.json', 'r') as file:
        return json.load(file)

def escribir_alumnos(alumnos):
    with open('alumnos.json', 'w') as file:
        json.dump(alumnos, file, indent=4)

@app.get("/alumnos/", response_model=List[Alumno])
def obtener_alumnos():
    return leer_alumnos()

@app.post("/alumnos/", response_model=Alumno)
def agregar_alumno(alumno: Alumno):
    alumnos = leer_alumnos()
    alumnos.append(alumno.dict())
    escribir_alumnos(alumnos)
    return alumno

@app.delete("/alumnos/{nombre}", response_model=Alumno)
def eliminar_alumno(nombre: str):
    alumnos = leer_alumnos()
    for i, alumno in enumerate(alumnos):
        if alumno['nombre'] == nombre:
            eliminado = alumnos.pop(i)
            escribir_alumnos(alumnos)
            return eliminado
    raise HTTPException(status_code=404, detail="Alumno no encontrado")