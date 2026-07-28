from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Hello from MindX DevOps Lab 🚀"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }