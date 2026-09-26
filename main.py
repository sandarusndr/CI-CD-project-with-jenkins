from fastapi import FastAPI

app = FastAPI(
    title="Ultimate CI/CD Python App",
    version="1.0.0"
)


@app.get("/")
def read_root():
    return {
        "message": "Ultimate CI/CD Pipeline using Python locally!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }