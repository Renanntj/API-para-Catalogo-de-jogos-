from models import db
from fastapi import HTTPException, Depends
from sqlalchemy.orm import sessionmaker, Session
from models.models_user import User
from jose import jwt, JWTError 
# importações que não estão sendo utilizadas estão aqui para verificação futura de token
def abrir_sessao():
    try:
        Session = sessionmaker(bind=db) # abrir sessao no banco de dados e fecha-la independente de qualquer coisa
        session = Session()
        yield
    finally:
        session.close()
