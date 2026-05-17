from fastapi import FastAPI

from menu import menu
from api.routes.order_routes import router

from api.database.connection import engine
from api.database.models import Base


app = FastAPI(title="Cyber Bar API")


@app.get("/")
def home():
    return {"message": "Welcome to ERROR 404 Cyber Bar API"}


@app.get("/menu")
def get_menu():
    return menu


app.include_router(router)


Base.metadata.create_all(bind=engine)