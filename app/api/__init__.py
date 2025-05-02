from .users import users_router 
from .products import products_router
from .auth import auth_router

__all__ = [
    "users_router",
    "products_router",
    "auth_router"]