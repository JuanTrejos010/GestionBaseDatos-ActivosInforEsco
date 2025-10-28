#Librerias para importar
from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
import psycopg2
import os
import uvicorn

#Plantillas

