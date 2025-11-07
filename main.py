#Librerias para importar
from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
import os
import uvicorn
from datetime import datetime

#Llamando otros módulos
from database import crear_Conexion, buscarSalas, buscarEquipo, registrarEquipo

#Se crean variables para las plantillas(templates)
templates = Jinja2Templates(directory="paginas")
app= FastAPI()
conn=crear_Conexion()

"""

Esta sección es para los recursos de frontend.

"""

#Llamando la raíz
@app.get("/")
def inicio(request: Request):
    return templates.TemplateResponse("inicio.html", {"request": request})

"""

Este es el listado de las tareas de CRUD como tal

"""
#Consulta de salas 
@app.get("/Salas/")
def ver_Salas():
    print("Busqueda de salas")
    resultado=buscarSalas(conn)
    return resultado

#Consulta de equipos
@app.get("/Equipos/")
def ver_Equipos():
    print("Buscando equipos: \n")
    resultado=buscarEquipo(conn)
    return resultado

@app.post("/Equipos/{e}")
def subir_Equipo():
    registrarEquipo(conn)
    print("Equipos registrados")
    return 0

#Ejecución del servidor
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)