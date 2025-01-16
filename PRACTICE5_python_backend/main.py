from typing import Optional
from fastapi import FastAPI
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