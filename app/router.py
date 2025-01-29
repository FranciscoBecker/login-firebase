from auth_service import verify_firebase_token
from fastapi import Depends, APIRouter

router = APIRouter()

###################################################
# ROTA PROTEGIDA PARA TESTAR A VALIDAÇÃO DO TOKEN #
###################################################

@router.get("/protected-route")
def protected_route(decoded_token=Depends(verify_firebase_token)):
    """
    Rota protegida que só pode ser acessada com um ‘token’ válido.
    """
    return {"message": "Token validado com sucesso!", "user_data": decoded_token}