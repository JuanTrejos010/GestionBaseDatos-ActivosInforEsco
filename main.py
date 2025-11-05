#Librerias para importar
from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
import os
import uvicorn

#Llamando otros módulos
from database import database

#Se crean variables para las plantillas(templates)
templates = Jinja2Templates(directory=".")
app= FastAPI()

#Llamando los recursos
@app.get("/")
def inicio(request: Request):
    return templates.TemplateResponse("inicio.html", {request: Request})

#Ejecución del servidor
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8005)