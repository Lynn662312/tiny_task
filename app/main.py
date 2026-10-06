from fastapi import FastAPI

app = FastAPI(title="Tiny Task", description="Lab 0 for self-learning")

@app.get("/health")
def health() -> dict[str,str]:
    return {"status": "ok"}

@app.get("/")
def home() -> dict[str,str]:
    return {"message": "Welcome to Tiny Task!"}

@app.post("/name")
def create_name() -> dict[str,str]:
    return {"name": "Tiny Task"}