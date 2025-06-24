# ----------------------------------------
# 🐍 Python Virtual Environment Setup
# ----------------------------------------
PYTHON := $(shell command -v python3 || command -v python)
VENV_DIR := .venv
VENV_ACTIVATE := . $(VENV_DIR)/bin/activate

ifeq ($(OS),Windows_NT)
    VENV_ACTIVATE := $(VENV_DIR)\Scripts\activate
endif

# ----------------------------------------
# 🔧 Project Tasks
# ----------------------------------------

.PHONY: venv
venv:
	$(PYTHON) -m venv $(VENV_DIR)

.PHONY: install
install: venv
	$(VENV_ACTIVATE) && pip install --upgrade pip
	$(VENV_ACTIVATE) && pip install -e .[dev]

.PHONY: run
run:
	$(VENV_ACTIVATE) && PYTHONPATH=. uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

.PHONY: test
test:
	$(VENV_ACTIVATE) && pytest --tb=short -q

.PHONY: lint
lint:
	$(VENV_ACTIVATE) && ruff app tests

.PHONY: format
format:
	$(VENV_ACTIVATE) && black app tests

.PHONY: check
check: lint format test

.PHONY: clean
clean:
	rm -rf $(VENV_DIR) __pycache__ */__pycache__ .pytest_cache .ruff_cache .mypy_cache .coverage dist *.egg-info

# ----------------------------------------
# 📦 Packaging (optional)
# ----------------------------------------

.PHONY: build
build:
	$(VENV_ACTIVATE) && python -m build

.PHONY: publish
publish: build
	$(VENV_ACTIVATE) && twine upload dist/*

# ----------------------------------------
# 📍 Utilities
# ----------------------------------------

.PHONY: help
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "🎯 Available targets:"
	@echo "  venv        Create virtual environment"
	@echo "  install     Install dependencies"
	@echo "  run         Run FastAPI app with Uvicorn"
	@echo "  test        Run tests with pytest"
	@echo "  lint        Run Ruff linting"
	@echo "  format      Run Black formatter"
	@echo "  check       Run all checks: lint, format, test"
	@echo "  clean       Clean up environment"
	@echo "  build       Build wheel and sdist"
	@echo "  publish     Upload to PyPI"
