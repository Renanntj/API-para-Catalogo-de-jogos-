from fastapi import FastAPI
from passlib.context import CryptContext
from routers.principal_router import router
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()

app.include_router(router)

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

