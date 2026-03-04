from fastapi import APIRouter

router = APIRouter(prefix="/principal", tags=["principal"])

@router.get("/")
async def tela_principal():
    return {
        "message":   "API para catalogo de jogos, posts e etc..."
    }
