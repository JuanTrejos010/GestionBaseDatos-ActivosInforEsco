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
templates = Jinja2Templates(directory=".")
app= FastAPI()
conn=crear_Conexion()

#######
#
#Esta sección es para los recursos de frontend.
#
#######

#Llamando la raíz
@app.get("/")
def inicio(request: Request):
    return templates.TemplateResponse("paginas/login/login.html", {"request": request})

@app.get("/loginScript.js")
def loginScript(request: Request):
    return templates.TemplateResponse("paginas/login/loginScript.js", {"request": request})

@app.get("/loginStyle.css")
def loginStyle(request: Request):
    return templates.TemplateResponse("paginas/login/loginStyle.css", {"request": request})

#Archivo de registro de equipos
@app.get("/interfaz")
def interfaz(request: Request):
    return templates.TemplateResponse("paginas/principal/index.html", {"request": request})

######
#
#Este es el listado de las tareas de CRUD como tal
#
######

#Consulta de salas 
@app.get("/salas/buscar")
def ver_Salas():
    print("Busqueda de salas")
    resultado=buscarSalas(conn)
    return resultado

#Consulta de equipos
@app.get("/equipos/buscar")
def ver_Equipos():
    print("Buscando equipos: \n")
    resultado=buscarEquipo(conn)
    return resultado

#Subir equipos
@app.post("/equipos/nuevo")
def subir_Equipo(
        marca:str= Form(...),
        modelo:str=Form(...),
        fecha_compra:str=Form(...),
        id_sala:int=Form(...)
        ):
    fecha_compra_dt=datetime.strptime(fecha_compra, "%Y-%m-%d").date()
    registrarEquipo(conn, marca, modelo, fecha_compra_dt, id_sala)
    print("Equipos registrados")
    return {"mensaje": "Equipo registrado correctamente"}



#Ejecución del servidor
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)