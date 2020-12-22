from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class CredencialIn(BaseModel):
    username    : str
    password    : str

    class Config:
        orm_mode = True

class PersonaUpdateIn(BaseModel):
    per_id:int
    per_nombre1:Optional[str] = None
    per_nombre2:Optional[str] = None
    per_apellido1:Optional[str] = None
    per_apellido2:Optional[str] = None
    per_fecha_nacimiento:Optional[datetime] = None
    per_nacionalidad:Optional[int] = None
    per_numero_contacto:Optional[str] = None
    per_direccion:Optional[str] = None
    per_ubicacion:Optional[int] = None
    per_otra:Optional[str] = None
    per_documento:Optional[int] = None
    per_numero:Optional[str] = None
    per_email:Optional[str] = None

    class Config:
        orm_mode = True

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

    class Config:
        orm_mode = True