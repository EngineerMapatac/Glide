from fastapi import FastAPI

app = FastAPI(title="Glide Diagnostic Engine API")

@app.get("/")
def read_root():
    return {"status": "operational", "message": "Glide engine is ready to analyze workflows."}

@app.get("/health")
def health_check():
    return {"status": "healthy"}