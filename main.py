#Librerias para importar
from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
import os
import uvicorn

#Llamando otros módulos
from database import crear_Conexion

#Se crean variables para las plantillas(templates)
templates = Jinja2Templates(directory=".")
app= FastAPI()
conn=crear_Conexion()

"""

Esta sección es para los recursos de frontend.

"""

#Llamando la raíz
@app.get("/")
def inicio(request: Request):
    return templates.TemplateResponse("inicio.html", {request: Request})

"""

Este es el listado de las tareas de CRUD como tal

"""
#Llamando 
@app.get("Salas/")
def tener_Salas():
    print("Busqueda de salas")
    
    return "Busqueda de salas"

#Ejecución del servidor
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)