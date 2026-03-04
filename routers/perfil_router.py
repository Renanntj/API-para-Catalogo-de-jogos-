from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["user"])

# criçao de user para exemplo, por enquanto so um teste, sem login

@router.post("/criar-usuario")
async def criar_user(): # criar usuario
    ...