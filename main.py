from fastapi import FastAPI
from app.config import include_routes
from app.exceptions.exception_handler import include_exceptions

app = FastAPI()
print('App started')
include_exceptions(app)
include_routes(app)


