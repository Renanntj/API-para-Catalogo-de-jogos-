from fastapi import APIRouter
from schemas.usuario import CriarUsuarioSchema
from fastapi import HTTPException, Depends, status
from dependecies.dependecies import abrir_sessao
from sqlalchemy.orm import Session
from models.models_user import User
from services.crypt_services import bcrypt_context
router_user = APIRouter(prefix="/user", tags=["user"])

# criçao de user para exemplo, por enquanto so um teste, sem login

@router_user.post("/criar-usuario", status_code=status.HTTP_201_CREATED)
async def criar_user(usuario_schema: CriarUsuarioSchema, session: Session = Depends(abrir_sessao)): # criar usuario
    verificar_usuario = session.query(User).filter(User.email==usuario_schema.email).first()
    if verificar_usuario:
        raise HTTPException(status_code=400, detail="Email de usuario existente")
    else:
        senha_segura = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = User(usuario_schema.nome, usuario_schema.usuario, usuario_schema.email, senha_segura)
        session.add(novo_usuario)
        session.commit()
    return {
        "message": f"Usuario adicionado com sucesso!",
        "nome": usuario_schema.nome,
        "email": usuario_schema.email 
    }