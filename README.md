# 🐳 Flask REST API — Dockerized & Deployed

A production-ready REST API built with Flask and containerized using Docker.
This project demonstrates a complete DevOps pipeline — from development to deployment.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.11 | Programming Language |
| Flask | REST API Framework |
| Docker | Containerization |
| Linux (Ubuntu) | Deployment Environment |
| GitHub | Version Control |

---

## 📁 Project Structure


flask-docker-app/
├── app.py              # Flask REST API with 4 endpoints
├── requirements.txt    # Python dependencies
├── Dockerfile          # Container image instructions
├── .dockerignore       # Files excluded from Docker image
└── README.md           # Project documentation


---

## 🚀 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | \`/\` | Home — API status check |
| GET | \`/api/items\` | Fetch all items |
| POST | \`/api/items\` | Add a new item |
| GET | \`/health\` | Health check for monitoring |

---

## ⚙️ Run Locally (Without Docker)

\`\`\`bash
git clone https://github.com/aliahmadshah56/flask-docker-app.git
cd flask-docker-app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
\`\`\`

API will be available at: \`http://localhost:5000\`

---

## 🐳 Run with Docker

\`\`\`bash
git clone https://github.com/aliahmadshah56/flask-docker-app.git
cd flask-docker-app
docker build -t flask-api:v1 .
docker run -d -p 5000:5000 --name my-flask-api flask-api:v1
curl http://localhost:5000/
\`\`\`

---

## 🧪 API Testing Examples

\`\`\`bash
curl http://localhost:5000/
curl http://localhost:5000/api/items
curl http://localhost:5000/health
curl -X POST http://localhost:5000/api/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Monitor", "price": 45000}'
\`\`\`

---

## 📋 Dockerfile Explained

\`\`\`dockerfile
FROM python:3.11-slim      # Lightweight base image (~150MB)
WORKDIR /app               # Set working directory inside container
COPY requirements.txt .    # Copy dependencies first (cache optimization)
RUN pip install --no-cache-dir -r requirements.txt  # Install dependencies
COPY . .                   # Copy application code
EXPOSE 5000                # Document the port
CMD ["python", "app.py"]   # Start the application
\`\`\`

---

## 🎯 Key DevOps Concepts Demonstrated

- ✅ **Containerization** — App packaged with all dependencies in Docker
- ✅ **Image Optimization** — Used slim base image and .dockerignore
- ✅ **Layer Caching** — requirements.txt copied before source code
- ✅ **Port Mapping** — Host to container port binding
- ✅ **Detached Mode** — Container runs in background
- ✅ **Health Check Endpoint** — \`/health\` route for monitoring
- ✅ **Version Control** — Full Git workflow with GitHub

---

## 👨‍💻 Author

**Ali Ahmad Shah**
BSCS Graduate — COMSATS University Islamabad
Aspiring DevOps Engineer

[![GitHub](https://img.shields.io/badge/GitHub-aliahmadshah56-black?logo=github)](https://github.com/aliahmadshah56)

---

## 📄 License

This project is open source and available under the MIT License.
