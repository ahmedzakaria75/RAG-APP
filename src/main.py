from fastapi import FastAPI

from dotenv import load_dotenv
from pathlib import Path
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

from routes import base_router


app = FastAPI()

app.include_router(base_router)

