from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class CredencialIn(BaseModel):
    username    : str
    password    : str

class PersonaOut(BaseModel):
    username    : str
    balance     : int

    class Config:
        orm_mode = True

class PersonUpdateIn(BaseModel):
    id:int
    nombre1:Optional[str] = None
    nombre2:Optional[str] = None
    apellido1:Optional[str] = None
    apellido2:Optional[str] = None
    fecha_nacimiento:Optional[datetime] = None
    nacionalidad:Optional[int] = None
    numeroDeContacto:Optional[str] = None
    direccion:Optional[str] = None
    ubicacion:Optional[int] = None
    otra:Optional[str] = None
    documento:Optional[int] = None
    numero:Optional[str] = None
    email:Optional[str] = None

class PersonaIdIn(BaseModel):
    id:int

class PersonaIn(BaseModel):
    per_nombre1:str
    per_nombre2:Optional[str] = ""
    per_apellido1:str
    per_apellido2:Optional[str] = ""
    per_fecha_nacimiento:Optional[datetime] = datetime(9999,12,31)
    per_nacionalidad:int
    per_numero_contacto:str
    per_direccion:Optional[str] = ""
    per_ubicacion:Optional[int] = 0
    per_otra:Optional[str] = ""
    per_documento:int
    per_numero:str
    per_email:str
    per_creado:datetime = datetime.now()
    per_modificado:datetime = datetime.now()