from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ..models import model_loader
from ..dependencies.config import conf
from ..dependencies.database import engine, Base
from ..routers import index as indexRoute 

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_loader.index()
indexRoute.load_routes(app)
