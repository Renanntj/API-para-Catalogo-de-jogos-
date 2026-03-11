from pydantic import BaseModel
from typing import Optional

class AutorSchema(BaseModel):
    usuario: str 
    class Config:
        from_attributes = True

class PublicacaoBase(BaseModel):
    titulo: str
    descricao: Optional[str] = None


class PublicacaoSchema(PublicacaoBase):
    id: int
    autor: AutorSchema

    class Config:
        from_attributes = True 