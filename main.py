from fastapi import FastAPI
from routers.principal_router import router
from routers.perfil_router import router_user
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()

app.include_router(router)
app.include_router(router_user)

