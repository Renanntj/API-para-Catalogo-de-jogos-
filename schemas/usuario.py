from pydantic import BaseModel
from typing import Optional

class CriarUsuarioSchema(BaseModel):
    nome : str
    usuario : str
    email : str
    senha : str
    admin : bool | None = False
    
    class Config:
        from_attributes = True
        
