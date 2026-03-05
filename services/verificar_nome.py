
def verificar_usuario_valido(usuario):
    
    if usuario != usuario.lower():
        return False
    
    
    simbolos_permitidos = "_-."
    
    
    for i in usuario:
        
        if not (i.isalnum() or i in simbolos_permitidos):
            return False
            
    return True

    