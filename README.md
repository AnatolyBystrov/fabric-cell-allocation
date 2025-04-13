# 📦 Fabric Cell Allocation

This project is a **warehouse cell allocator** written in Python 🐍, which determines the optimal storage cell for products based on specific attributes like quantity, cooling, and hazard requirements.

---

## 🚀 Features

- ✅ Product placement logic based on type and quantity
- ✅ Constraints: hazardous / cooling / regular zones
- ✅ Fully automated unit tests
- ✅ Docker support
- ✅ Kubernetes deployment ready

---

## 📁 Project Structure

. ├── app/ │ ├── init.py │ ├── cell.py │ ├── product.py │ ├── product_catalog.py │ ├── test_allocation.py │ └── warehouse.py ├── Dockerfile ├── docker-compose.yml └── k8s/ └── deployment.yaml


---

## 🧪 Running Tests

### Locally

```bash
PYTHONPATH=. python3 app/test_allocation.py
docker compose up --build
kubectl apply -f k8s/deployment.yaml
kubectl get pods
kubectl logs -l app=fabric-cell-allocator

🛠 Technologies
Python 3.11

Docker

Kubernetes

GitHub Actions (CI/CD ready)

📌 Future Ideas
Add REST API interface (FastAPI)

Integrate database for persistent storage

Add monitoring (Prometheus / Grafana)

👨‍💻 Author
Anatoly Bystrov
💼 Full-Stack Developer
🌍 GitHub

