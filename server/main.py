from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import executor

app = FastAPI()

origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

app.include_router(executor.router)