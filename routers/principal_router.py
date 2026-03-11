from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.models_post import Publicacoes
from schemas.posts import PublicacaoSchema
from dependecies.dependecies import abrir_sessao, verificar_token


router = APIRouter(prefix="/principal", tags=["principal"])

@router.get("/publicacoes", response_model=List[PublicacaoSchema])
def listar_publicacoes(db: Session = Depends(abrir_sessao)):
    publicacoes = db.query(Publicacoes).all()
    return publicacoes