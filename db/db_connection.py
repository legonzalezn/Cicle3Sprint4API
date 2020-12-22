from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#host="ec2-35-168-77-215.compute-1.amazonaws.com"
#port="5432"
#user="mzmxdxnaujiwlc"
#password="5ade34f1f274423c7f2906f21a38c300f2deaa7f862c87d2ec10dc861ee91541"
#database="d7ltlkbo6pddqf"
#schema = "Reservas"

engine = create_engine("postgresql://mzmxdxnaujiwlc:5ade34f1f274423c7f2906f21a38c300f2deaa7f862c87d2ec10dc861ee91541@ec2-35-168-77-215.compute-1.amazonaws.com:5432/d7ltlkbo6pddqf")

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()
Base.metadata.schema = schema
