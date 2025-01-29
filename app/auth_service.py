from firebase_admin import credentials, auth, initialize_app
from fastapi import Header, HTTPException


# Inicializar o Firebase Admin SDK
cred = credentials.Certificate("C:/Users/W027224/Documents/login-firebase/resources/serviceAccountKey.json")
initialize_app(cred)

def verify_firebase_token(authorization: str = Header(...)):
    """
    Middleware para verificar o token do Firebase enviado no cabeçalho 'Authorization'.
    """
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Cabeçalho Authorization inválido.")

    id_token = authorization.split("Bearer ")[1]

    try:
        # Valida e decodifica o token do Firebase
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token  # Retorna os dados do usuário autenticado
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Token inválido: {str(e)}")