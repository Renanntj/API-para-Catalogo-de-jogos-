from fastapi import APIRouter, Response
from fastapi import HTTPException, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from dependecies.dependecies import abrir_sessao, verificar_token
from typing import Optional
from models.models_post import Publicacoes
from models.models_user import User
router_posts = APIRouter(prefix="/posts", tags=["posts"], dependencies=[Depends(verificar_token)])

@router_posts.get("/publicacao/{pub_id}/imagem")
def get_imagem_publicacao(pub_id: int, db: Session = Depends(abrir_sessao)):
    pub = db.query(Publicacoes).filter(Publicacoes.id == pub_id).first()
    
    if not pub or not pub.imagem:
        raise HTTPException(status_code=404, detail="Imagem ou não encontrada")
    return Response(content=pub.imagem, media_type="image/jpeg")

@router_posts.post("/criar-post", status_code=201)
async def criar_post(
    titulo: str = Form(...),
    descricao: Optional[str] = Form(None),
    arquivo: UploadFile = File(None),
    db: Session = Depends(abrir_sessao),
    usuario_logado: User = Depends(verificar_token) 
):
    conteudo_binario = await arquivo.read() if arquivo else None
        
    nova_pub = Publicacoes(
        titulo=titulo,
        descricao=descricao,
        imagem=conteudo_binario, 
        autor_id=usuario_logado.id  
    )
    
    db.add(nova_pub)
    db.commit()
    db.refresh(nova_pub)
    return nova_pub
