from fastapi import FastAPI
import executor

app = FastAPI()

app.include_router(executor.router)