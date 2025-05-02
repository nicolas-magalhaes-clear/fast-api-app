from fastapi import FastAPI
from app.config import include_routes
from app.exceptions.exception_handler import include_exceptions
from fastapi.middleware.cors import CORSMiddleware
from app.config.constants import constants

app = FastAPI()

app.add_middleware(CORSMiddleware, 
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
  expose_headers=["*"]
)

include_exceptions(app)
include_routes(app)


