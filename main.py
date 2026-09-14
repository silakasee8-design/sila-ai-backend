from fastapi import FastAPI

app = FastAPI(title="Sila AI Backend")


@app.get("/")
def home():
    return {
        "message": "Sila AI Backend is running!",
        "status": "online"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
