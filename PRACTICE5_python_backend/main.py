from typing import List, Optional
import uuid
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Inicializacion de variable con caracteristicas de una API REST.
app = FastAPI()

# Definicion del modelo de la base de datos.
class Course(BaseModel):
    id: Optional[str] = None
    name: str
    description: Optional[str] = None
    level: str
    duration: int

# Simulacion de la base de datos.
courses_db = []

# CRUD

## Read con GET (all).
@app.get('/courses/', response_model = List[Course])
def get_courses():
    return courses_db

## Read con Get (id).
@app.get('/courses/{id}', response_model = Course)
def get_course(id:str):
    ## next() toma la primera coincidencia del array devuelto.
    course = next((course for course in courses_db if course.id == id), None)
    if course is None:
        raise HTTPException(status_code = 404, detail = 'course not found')
    return course

## Create con POST.
@app.post('/courses/', response_model = Course)
def create_course(course: Course):
    ## uuid se encarga de generar un id unico.
    course.id = str(uuid.uuid4())
    courses_db.append(course)
    return course

## Update con PUT.
@app.put('/courses/{id}', response_model = Course)
def update_course(id:str, course_updated:Course):
    course = next((course for course in courses_db if course.id == id), None)
    if course is None:
        raise HTTPException(status_code = 404, detail = 'course not found')
    course_updated.id = id
    ## Buscamos en indice exacto del curso a actualizar con index() en la base de datos (courses_db).
    index = courses_db.index(course)
    courses_db[index] = course_updated
    return course_updated

## Eliminar con DELETE.
@app.delete('/courses/{id}', response_model = Course)
def delete_course(id:str):
    course = next((course for course in courses_db if course.id == id), None)
    if course is None:
        raise HTTPException(status_code = 404, detail = 'course not found')
    courses_db.remove(course)
    return course

