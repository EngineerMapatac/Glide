from fastapi import FastAPI
from database import engine, Base
import models

# Generate database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Glide Diagnostic Engine API")

@app.get("/")
def read_root():
    return {"status": "operational", "message": "Glide engine is ready."}