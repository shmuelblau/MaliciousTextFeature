
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from models.config import *
from models.Manager import Manager
from models.logger import get_logger

log = get_logger()

app = FastAPI()


@app.get("/")
def home():
    pass

@app.get("/")
def home1():
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)