from fastapi import APIRouter
from server.routes.apis import *

api_router = APIRouter()

api_router.include_router(route_api.router)