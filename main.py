from fastapi import Depends, FastAPI
from routers.persona_router import reservas as router_personas

api = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

workspace=[[
    "http://localhost.tiangolo.com"
    , "https://localhost.tiangolo.com"
    , "http://localhost"
    , "http://localhost:8080"
    , "http://127.0.0.1:8080"
    , "http://127.0.0.1"
],[
    "https://reserva-hotel-appvue.herokuapp.com/"
    , "http://190.69.231.174"
]]

origins = workspace[1]

api.add_middleware(
    CORSMiddleware
    , allow_origins=origins
    , allow_credentials=True
    , allow_methods=["*"]
    , allow_headers=["*"]
)

api.include_router(router_personas)