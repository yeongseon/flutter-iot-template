# Flutter IoT Template

A full-stack monorepo template for building Flutter + Python (FastAPI) + Edge IoT applications.

This template is designed for rapid prototyping and educational use cases involving:
- A mobile app (Flutter)
- A backend API (FastAPI)
- An edge device client (e.g. Jetson Nano, Raspberry Pi)

---

## 📁 Project Structure

```
flutter-iot-template/
├── flutter_app/     # Flutter mobile app
├── backend/         # FastAPI backend server
├── edge_client/     # Python edge client (Jetson/Raspberry Pi)
├── docker-compose.yml
├── Makefile
└── .github/workflows/ (CI/CD setup)
```

---

## 🚀 Quick Start

### 1. Clone this repo

```bash
git clone https://github.com/yeongseon/flutter-iot-template.git
cd flutter-iot-template
```

### 2. Start backend and edge client (Docker)

```bash
docker compose up --build
```

- `backend`: accessible at http://localhost:8000/hello
- `edge_client`: prints "Hello from Edge Client!" every 5 seconds

### 3. Run Flutter app

Follow instructions in [`flutter_app/README.md`](./flutter_app/README.md)

---

## 🔗 Component Overviews

- [`flutter_app`](./flutter_app): Flutter UI with FastAPI integration via `http` package
- [`backend`](./backend): FastAPI backend with a `/hello` endpoint
- [`edge_client`](./edge_client): Python script that simulates edge behavior (e.g. sensor logging)

---

## 📦 Requirements

- Docker + Docker Compose
- Flutter SDK 3.0+
- Python 3.9+ (for local backend testing)

---

## 📄 License

MIT License
