from fastapi import FastAPI
import login_router, router

app = FastAPI()

app.include_router(router.router)
app.include_router(login_router.login_router)
