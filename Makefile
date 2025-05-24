# Makefile at root of flutter-iot-template

FLUTTER=flutter/bin/flutter

# Flutter commands
flutter-run:
	cd flutter_app && ../$(FLUTTER) run

flutter-build:
	cd flutter_app && ../$(FLUTTER) build apk

flutter-clean:
	cd flutter_app && ../$(FLUTTER) clean

flutter-get:
	cd flutter_app && ../$(FLUTTER) pub get

# Docker Compose commands
up:
	docker-compose up --build

down:
	docker-compose down

build:
	docker-compose build

logs:
	docker-compose logs -f edge_client backend

restart:
	make down && make up
