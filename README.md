# Flask REST API — Dockerized & Deployed

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-black?logo=flask)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange?logo=linux)
![GitHub](https://img.shields.io/badge/GitHub-Version%20Control-black?logo=github)

A production-ready REST API built with Flask and containerized using Docker — demonstrating a complete DevOps pipeline from local development to containerized deployment on a Linux server.

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.11 | Core Language |
| Flask | REST API Framework |
| Docker | Containerization |
| Linux (Ubuntu) | Deployment OS |
| GitHub | Version Control |

---

## Project Structure

```
flask-docker-app/
├── app/
│   └── app.py              # Flask REST API — 4 endpoints
├── docker/
│   └── Dockerfile          # Container image instructions
├── requirements.txt        # Python dependencies
├── .dockerignore           # Files excluded from Docker image
└── README.md               # Project documentation
```

---

## API Endpoints

| Method | Endpoint | Description | Response |
|--------|----------|-------------|----------|
| GET | `/` | Home — API status check | 200 |
| GET | `/api/items` | Fetch all items | 200 |
| POST | `/api/items` | Add a new item | 201 |
| GET | `/health` | Health check for monitoring | 200 |

---

## Run Locally (Without Docker)

```bash
# Clone the repository
git clone https://github.com/aliahmadshah56/flask-docker-app.git
cd flask-docker-app

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the server
python app/app.py
```

> API will be available at: `http://localhost:5000`

---

## Run with Docker

```bash
# Clone the repository
git clone https://github.com/aliahmadshah56/flask-docker-app.git
cd flask-docker-app

# Build Docker image
docker build -f docker/Dockerfile -t flask-api:v1 .

# Run container
docker run -d -p 5000:5000 --name my-flask-api flask-api:v1
```

> API will be available at: `http://localhost:5000`

---

## API Testing

```bash
# Home
curl http://localhost:5000/

# Get all items
curl http://localhost:5000/api/items

# Health check
curl http://localhost:5000/health

# Add new item
curl -X POST http://localhost:5000/api/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Monitor", "price": 45000}'
```

### Sample Responses

**GET /**
```json
{
  "message": "Flask REST API is running!",
  "status": "healthy"
}
```

**GET /api/items**
```json
{
  "items": [
    {"id": 1, "name": "Laptop", "price": 150000},
    {"id": 2, "name": "Mouse", "price": 2500},
    {"id": 3, "name": "Keyboard", "price": 4000}
  ],
  "total": 3
}
```

**POST /api/items**
```json
{
  "item": {"name": "Monitor", "price": 45000},
  "message": "Item added successfully"
}
```

---

## Docker Commands Reference

```bash
# Build image
docker build -f docker/Dockerfile -t flask-api:v1 .

# Run container in background
docker run -d -p 5000:5000 --name my-flask-api flask-api:v1

# View running containers
docker ps

# View container logs
docker logs my-flask-api

# Stop container
docker stop my-flask-api

# Remove container
docker rm my-flask-api

# Remove image
docker rmi flask-api:v1
```

---

## DevOps Concepts Demonstrated

| Concept | Implementation |
|---------|----------------|
| Containerization | App packaged with all dependencies using Docker |
| Image Optimization | `python:3.11-slim` base image reduces size to ~150MB |
| Layer Caching | `requirements.txt` copied before source code for faster builds |
| Port Mapping | Host port `5000` → Container port `5000` |
| Detached Mode | Container runs in background using `-d` flag |
| Health Monitoring | Dedicated `/health` endpoint for uptime checks |
| Version Control | Git + GitHub with structured commit messages |

---

## Author

**Ali Ahmad Shah**  
BSCS Graduate — COMSATS University Islamabad, Vehari Campus  
Aspiring DevOps Engineer

[![GitHub](https://img.shields.io/badge/GitHub-aliahmadshah56-black?logo=github)](https://github.com/aliahmadshah56)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://linkedin.com/in/aliahmadshah56)

---

## License

This project is open source and available under the [MIT License](LICENSE).
