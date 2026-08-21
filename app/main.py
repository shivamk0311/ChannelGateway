from fastapi import FastAPI
from app.core import config

app = FastAPI(title=config.app_name)

@app.get("/health")
def status():
    return { "status" : "ok" }
