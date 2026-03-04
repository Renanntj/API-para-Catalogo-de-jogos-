from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["user"])

# @router.get("/")
# async def tela_principal():
#     return {
#         "message" "API para catalogo de jogos, posts e etc..."
#     }
