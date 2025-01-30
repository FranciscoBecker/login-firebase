import pyrebase
from fastapi import APIRouter, HTTPException
from schema import UserData
import json
from firebase_admin import auth

########################################################
# ROTAS PARA CADASTRAR UM USUÁRIO E PARA FAZER LOGIN   #
# EM UM PROJETO REAL, ESSAS FUNÇÕES FICAM NO FRONT END #
########################################################

# CONFIGURAÇÃO DO PYREBASE ------------------------------------------------------------------------#
with open("C:/Users/W027224/Documents/login-firebase/resources/firebaseConfig.json", "r") as f:
    config = json.load(f)

pyrebase = pyrebase.initialize_app(config)
pyrebase_auth = pyrebase.auth()
# -------------------------------------------------------------------------------------------------#

login_router = APIRouter()


@login_router.post("/login")
def login_route(user_data: UserData):
    try:
        login = pyrebase_auth.sign_in_with_email_and_password(user_data.email, user_data.password)
        print(login)
        return login
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))


@login_router.post("/signup")
def signup(user_data: UserData):
    try:
        # CRIANDO USUÁRIO COM O PYREBASE
        # user = pyrebase_auth.create_user_with_email_and_password(user_data.email, user_data.password)
        # CRIANDO USUÁRIO COM O FIREBASE_ADMIN
        user = auth.create_user(
            email=user_data.email,
            email_verified=False,
            phone_number=user_data.phone_number,
            password=user_data.password,
            display_name=user_data.display_name,
            photo_url=user_data.photo_url,
            disabled=False
        )

        print(user)
        return user
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
