from models.models import Base, user_games_association
from sqlalchemy import Column, String, Integer, Float, LargeBinary
from sqlalchemy.orm import relationship
class Jogos(Base):
    __tablename__= "jogos"
    
    #um jogo tera nome, duracao, uma foto e uma nota.
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False, index=True)
    duracao = Column(Float, nullable=False) # duracao horas
    foto_capa = Column(LargeBinary, nullable=True)
    nota = Column(Float)
    usuarios = relationship("User", secondary=user_games_association, back_populates="jogos")
    