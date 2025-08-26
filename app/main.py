from fastapi import FastAPI

app = FastAPI(title="Frenemy AI")

@app.get("/")
def read_root():
    return {"message": "Welcome to Frenemy AI (More of a friend than an enemy 😜)"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "version": "0.1.0"}