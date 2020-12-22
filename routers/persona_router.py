from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import exc
from sqlalchemy import desc
from db.db_connection import get_db
from db.persona_db import PersonaCredencialInDB, PersonaInDB
#from db.transaction_db import TransactionInDB
from models.persona_models import CredencialIn, PersonaOut,PersonaIdIn,PersonaIn
from routers.auxiliar import mensaje
#from models.transaction_models import TransactionIn, TransactionOut

reservas = APIRouter()

@reservas.post("/user/auth")
async def auth_user(user_in: CredencialIn, db: Session = Depends(get_db)):

    user_in_db = db.query(PersonaCredencialInDB).filter(PersonaCredencialInDB.per_cre_nickname == user_in.username).first()

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    
    if not user_in_db.per_cre_contrasegna == user_in.password:
        raise HTTPException(status_code=403, detail="Error de autenticacion")

    return  {"Autenticado": True}

@reservas.get("/user")
async def get_person(person_in:PersonaIdIn, db: Session = Depends(get_db)):
    user_in_db = db.query(PersonaInDB).get(person_in.id)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail = mensaje(1,"usuario"))
    else:
        person_out = user_in_db
        return person_out

@reservas.get("/user/list")
async def get_list_person(db: Session = Depends(get_db)):
    person_in_db = db.query(PersonaInDB).all()
    if person_in_db == None:
        raise HTTPException(status_code=404, detail = message(2,"usuarios"))
    else:
        return person_in_db

@reservas.post("/user/add")
async def post_person(person_in:PersonaIn, db: Session = Depends(get_db)):
    person_in_aux = person_in
    db.begin()
    db.add(PersonaInDB(**person_in_aux.dict()))
    try:
        db.commit()
        person_in_db = db.query(PersonaInDB).order_by(desc(PersonaInDB.per_id)).first()
        return person_in_db
    except exc.SQLAlchemyError as e:
        raise HTTPException(status_code=404, detail = mensaje(5,str(e.__dict__['orig']),"BD"))
        db.rollback()
        return None

@reservas.delete("/user/delete")
async def del_person(person_in:PersonaIdIn, db: Session = Depends(get_db)):
    person_in_db = db.query(PersonaInDB).filter(PersonaInDB.per_id == person_in.id).first()
    if person_in_db == None:
        raise HTTPException(status_code=404, detail = mensaje(1,"usuario"))
    else:
        db.query(PersonaInDB).filter(PersonaInDB.per_id == person_in.id).delete()
        db.commit()
        person_count = db.query(PersonaInDB).count()
        return {"Total":person_count}

"""
@reservas.get("/person/full_name/")
async def get_full_name(person_in:PersonIdIn):
    person_in_db = get_person_full(person_in.id)
    if person_in_db == None:
        raise HTTPException(status_code=404, detail = message(1,"usuario"))
    else:
        person_out = PersonNameFullOut(**{"name":get_name_full(person_in_db.id)})
        return person_out



@reservas.put("/update/person/")
async def put_person(person_in:PersonUpdateIn):
    updated = False
    person_in_db = get_person_full(person_in.id)
    if person_in_db == None:
        raise HTTPException(status_code=404, detail = message(1,"usuario"))
    else:
        person_in_db = person_in_db.dict()
        for personk, personv in person_in.dict().items():
            if personv != None:
                if person_in_db[personk] != personv:
                    person_in_db[personk] = personv
                    updated = True
        if updated:
            person_in_db = update_person(person_in_db)
            person_out = PersonOut(**person_in_db)
            return person_out
        else:
            raise HTTPException(status_code=404, detail = mensaje(4))


"""