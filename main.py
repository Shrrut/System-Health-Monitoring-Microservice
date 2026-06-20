from fastapi import FastAPI
import psutil

app = FastAPI()

@app.get("/health")
def get_health():
    return {
        "status": "healthy",
        "cpu_percent": psutil.cpu_percent(interval=1),
        "ram_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent
    }