from sqlalchemy import Table
from db.db_connection import Base, engine

class PersonaCredencialInDB(Base):
    __table__ = Table(
        'personas_credenciales',
        Base.metadata,
        autoload_with = engine,
        autoload = True,
        schema = Base.metadata.schema
    )

class PersonaInDB(Base):
    __table__ = Table(
        'personas',
        Base.metadata,
        autoload_with = engine,
        autoload = True,
        schema = Base.metadata.schema
    )