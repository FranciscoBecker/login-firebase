from fastapi import FastAPI
import login_router, router
import uvicorn

app = FastAPI()

app.include_router(router.router)
app.include_router(login_router.login_router)

if __name__ == '__main__':
    uvicorn.run(app, reload=True, host='localhost',
                port=8000, log_level='debug', workers=1)