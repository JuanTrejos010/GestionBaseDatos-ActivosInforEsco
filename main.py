#Librerias para importar
from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
import psycopg2
import os
import uvicorn

#Plantillas
from database import database

#Se crean variables para las plantillas(templates)
templates = Jinja2Templates(directory=".")
app= FastAPI()
