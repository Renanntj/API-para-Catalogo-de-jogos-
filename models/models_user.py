from models.models import Base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = "usuario"
    
    id = Column(Integer, primary_key=True, autoincrement=True)    
    nome = Column(String, nullable=False)
    usuario = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    senha = Column(String, nullable=False)
    jogos = Column(String)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    
    # def __str__(self, nome, usuario, email, senha):
    #     self.nome = nome
    #     self.usuario = usuario
    #     self.email = email
    #     self.senha = senha

    
    