from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "MindX Docker Compose 🚀"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }