#Librerias para importar
from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os
import uvicorn
from datetime import datetime

#Llamando otros módulos
from database import crear_Conexion, Password, buscarSalas, buscarEquipo, registrarEquipo, eliminarEquipo

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
def loginScript():
    return FileResponse("paginas/login/loginScript.js", media_type="application/javascript")

@app.get("/loginStyle.css")
def loginStyle():
    return FileResponse("paginas/login/loginStyle.css")

@app.get("/Script.js")
def Script():
    return FileResponse("paginas/principal/Script.js", media_type="application/javascript")

@app.get("/Style.css")
def Style():
    return FileResponse("paginas/principal/Style.css")

#Archivo de registro de equipos
@app.get("/interfaz")
def interfaz(request: Request):
    return templates.TemplateResponse("paginas/principal/index.html", {"request": request})

#Usuarios 
USERS = {
    "estudiante@liceo.com": "Estu1234!",
    "docente@liceo.com": "Docente2025"
}

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
        nombre:str= Form(...),
        marca:str= Form(...),
        modelo:str=Form(...),
        fecha_compra:str=Form(...),
        id_sala:int=Form(...)
        ):
    fecha_compra_dt=datetime.strptime(fecha_compra, "%Y-%m-%d").date()
    registrarEquipo(conn, nombre, marca, modelo, fecha_compra_dt, id_sala)
    print("Equipos registrados")
    return {"mensaje": "Equipo registrado correctamente"}

#Eliminar equipos
@app.post("/equipos/eliminar")
def eliminar_equipo(id_equipo: int = Form(...)):
    eliminarEquipo(conn, id_equipo)
    return {"mensaje": "Equipo eliminado correctamente"}

#Login
@app.post("/login")
def login(email: str = Form(...), password: str = Form(...)):
    row=Password(conn, email)
    if row and row[0] == password:
        return {"success": True, "email": email}
    else:
        return {"success": False}

#Ejecución del servidor
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)