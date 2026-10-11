# System Health & Monitoring Microservice

A lightweight, asynchronous REST API built with FastAPI that serves hardware telemetry. It is designed for CI/CD pipeline verification and containerized monitoring environments.

## Features
- **Real-time telemetry:** Reports CPU, RAM, and disk utilization using `psutil`.
- **Asynchronous framework:** Built on FastAPI and Uvicorn for non-blocking request handling.
- **Minimal footprint:** Uses a `python:3.10-slim` Docker base image for fast container startup and a small attack surface.
- **Pipeline integration:** Exposes a `/health` endpoint suited to automated pipeline checks and Kubernetes probes.

## Technologies Used
- **Application framework:** Python, FastAPI, Uvicorn
- **System monitoring:** `psutil`
- **Containerization:** Docker

## Getting Started

### Prerequisites
- Python 3.10+
- Docker

### Local Development
1. Install dependencies:
```bash
   pip install -r requirements.txt
```
2. Start the Uvicorn server:
```bash
   python -m uvicorn main:app --host 0.0.0.0 --port 8000
```
3. Check the telemetry endpoint in your browser or with curl:
```bash
   curl http://localhost:8000/health
```

### Docker Deployment
1. Build the image:
```bash
   docker build -t system-health-api .
```
2. Run the container:
```bash
   docker run -p 8000:8000 system-health-api
```
3. Access the API at http://localhost:8000/health.
