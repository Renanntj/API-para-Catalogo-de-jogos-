from fastapi import APIRouter
from schemas.usuario import CriarUsuarioSchema
from fastapi import HTTPException, Depends, status
from dependecies.dependecies import abrir_sessao
from sqlalchemy.orm import Session
from models.models_user import User
from services.crypt_services import gerar_senha_hash
from services.verificar_nome import verificar_usuario_valido
router_user = APIRouter(prefix="/user", tags=["user"])

# criçao de user para exemplo, por enquanto so um teste, sem login

@router_user.post("/criar-usuario", status_code=status.HTTP_201_CREATED)
async def criar_user(usuario_schema: CriarUsuarioSchema, session: Session = Depends(abrir_sessao)): # criar usuario
    verificar_usuario = session.query(User).filter(User.email==usuario_schema.email).first()
     
    if verificar_usuario:
        raise HTTPException(status_code=400, detail="Email de usuario existente")
    
    else:
        verificar_username = session.query(User).filter(User.usuario==usuario_schema.usuario).first()
        if verificar_username:
            raise HTTPException(status_code=400, detail="Nome de usuario existente")
        
        elif not verificar_usuario_valido(usuario_schema.usuario):
            raise HTTPException(status_code=400, detail={
                "message": "Nome de usuario deve ser minusculo, ter apenas nome, numero e '_', '-' e '.'"
            })
        senha_segura = gerar_senha_hash(usuario_schema.senha)
        novo_usuario = User(usuario_schema.nome, usuario_schema.usuario, usuario_schema.email, senha_segura)
        session.add(novo_usuario)
        session.commit()
        return {
            "message": f"Usuario adicionado com sucesso!",
            "nome": usuario_schema.nome,
            "email": usuario_schema.email 
        }

@router_user.get("/ver-perfil/{username}")
async def ver_perfil_publico(username: str, session: Session = Depends(abrir_sessao)): # aqui será para ver o perfil (visita de perfil)
    perfil = session.query(User).filter(User.usuario==username).first()
    if not perfil:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")
    
    return {
        "Nome": perfil.nome,
        "Usuario": perfil.usuario
    }
    