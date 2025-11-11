#Llamando la libreria Pydantic
import string
from pydantic import BaseModel

class Usuario(BaseModel):
    id: int
    nombre: string
    edad: int
    is_admin: bool
