from models.models import Base
from sqlalchemy import Column, String, Integer, Float, LargeBinary

class Jogos(Base):
    __tablename__= "jogos"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False, index=True)
    duracao = Column(Float, nullable=False) # duracao horas
    foto_capa = Column(LargeBinary, nullable=True)
    nota = Column(Float)
    
    # def __str__(self, nome, duracao, nota, foto_capa):
    #     self.nome = nome
    #     self.duracao = duracao
    #     self.nota = nota
    #     self.foto_capa = foto_capa
    