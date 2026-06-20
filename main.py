@app.get("/health")
def get_health():
    return {
        "status": "healthy",
        "message": "My CI/CD pipeline is working!", # <-- Add this line
        "cpu_percent": psutil.cpu_percent(interval=1),
        "ram_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent
    }