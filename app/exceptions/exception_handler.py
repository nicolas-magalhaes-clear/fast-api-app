# pyright: reportUnusedFunction=false
from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from app.exceptions.exceptions_types.unauthorized_exception import UnauthorizedException


def include_exceptions(app: FastAPI):
    @app.exception_handler(UnauthorizedException)
    async def unauthorized_exception_handler(request: Request, exc: UnauthorizedException):
      return JSONResponse(
        status_code=401,
        content={
          'detail': exc.message
        }
      )
