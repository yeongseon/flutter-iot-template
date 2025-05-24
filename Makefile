FLUTTER=flutter/bin/flutter

# Compose detection: prefer podman-compose, fallback to 'docker compose'
COMPOSE_CMD=$(shell command -v podman-compose >/dev/null 2>&1 && echo podman-compose || echo "docker compose")

# Flutter commands
flutter-run:
	cd flutter_app && ../$(FLUTTER) run

flutter-build:
	cd flutter_app && ../$(FLUTTER) build apk

flutter-clean:
	cd flutter_app && ../$(FLUTTER) clean

flutter-get:
	cd flutter_app && ../$(FLUTTER) pub get

# Compose commands
up:
	$(COMPOSE_CMD) up --build

down:
	$(COMPOSE_CMD) down

build:
	$(COMPOSE_CMD) build

logs:
	$(COMPOSE_CMD) logs -f edge_client backend

restart:
	$(MAKE) down
	$(MAKE) up

# Optional: Start podman machine
podman-start:
	podman machine start || true
