import pyrebase
from fastapi import APIRouter
from schema import UserData
import json

########################################################
# ROTAS PARA CADASTRAR UM USUÁRIO E PARA FAZER LOGIN   #
# EM UM PROJETO REAL, ESSAS FUNÇÕES FICAM NO FRONT END #
########################################################

with open("C:/Users/W027224/Documents/login-firebase/resources/firebaseConfig.json", "r") as f:
    config = json.load(f)

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

login_router = APIRouter()

@login_router.post("/login")
def login_route(user_data: UserData):
    try:
        login = auth.sign_in_with_email_and_password(user_data.email, user_data.password)
        print(login)
        return login
    except Exception as e:
        print(e)
    return

@login_router.post("/signup")
def signup(user_data: UserData):
    try:
        user = auth.create_user_with_email_and_password(user_data.email, user_data.password)
        print(user)
        return user
    except Exception as e:
        print(e)
    return