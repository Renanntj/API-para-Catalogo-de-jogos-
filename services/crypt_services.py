import bcrypt

def gerar_senha_hash(senha: str) -> str:
    senha_bytes = senha.encode('utf-8')
    salt = bcrypt.gensalt()
    hash_senha = bcrypt.hashpw(senha_bytes, salt)
    return hash_senha.decode('utf-8')

def verificar_senha(senha_plana: str, senha_hash: str) -> bool:
    return bcrypt.checkpw(
        senha_plana.encode('utf-8'), 
        senha_hash.encode('utf-8')
    )