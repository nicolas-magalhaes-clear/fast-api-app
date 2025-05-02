from fastapi import FastAPI
from app.api import users_router, products_router


def include_routes(app : FastAPI):
  app.include_router(users_router, prefix="/users", tags=["users"])
  app.include_router(products_router, prefix="/products", tags=["products"])