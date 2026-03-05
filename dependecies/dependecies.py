from models.models import DATABASE_URL
from fastapi import HTTPException, Depends
from sqlalchemy.orm import sessionmaker, Session
from models.models_user import User
from jose import jwt, JWTError 
# importações que não estão sendo utilizadas estão aqui para verificação futura de token
def abrir_sessao():
    try:
        Session = sessionmaker(bind=DATABASE_URL) # abrir sessao no banco de dados e fecha-la independente de qualquer coisa
        session = Session()
        yield session
    finally:
        session.close()
