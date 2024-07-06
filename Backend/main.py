from fastapi import FastAPI
from dotenv import load_dotenv
from Routes.usuario_routes import usuario_routes
from Routes.webhook import webhook

app=FastAPI()

app.include_router(usuario_routes,prefix="/usuario")
app.include_router(webhook,prefix="/webhook")
load_dotenv()
