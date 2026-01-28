.PHONY: help install install-dev format lint typecheck test test-all run run-docker up down clean \
        health echo echo-invalid root

# -------------------------------------------------
# Variables
# -------------------------------------------------
APP_NAME = pystartertemplate
HOST = http://localhost:8000
API_V1 = $(HOST)/api/v1

# -------------------------------------------------
# Help
# -------------------------------------------------
help:
	@echo ""
	@echo "📦 pystartertemplate - Kullanılabilir Make Komutları"
	@echo ""
	@echo "🔧 Kurulum"
	@echo "  make install        → Uygulama bağımlılıklarını kurar"
	@echo "  make install-dev    → Dev + test bağımlılıklarını kurar"
	@echo ""
	@echo "▶️  Çalıştırma"
	@echo "  make run            → Local FastAPI server (reload)"
	@echo "  make up             → Docker Compose ile başlat"
	@echo "  make down           → Docker Compose durdur"
	@echo ""
	@echo "🧪 Test & Kalite"
	@echo "  make format         → Black + Ruff (fix)"
	@echo "  make lint           → Ruff (check)"
	@echo "  make typecheck      → Mypy"
	@echo "  make test           → Pytest"
	@echo "  make test-all       → Format + Lint + Typecheck + Test"
	@echo ""
	@echo "🌐 API Endpoint Testleri"
	@echo "  make root           → GET /"
	@echo "  make health         → GET /api/v1/health"
	@echo "  make echo           → POST /api/v1/echo (valid)"
	@echo "  make echo-invalid   → POST /api/v1/echo (invalid body)"
	@echo ""
	@echo "🧹 Temizlik"
	@echo "  make clean          → Cache ve geçici dosyaları sil"
	@echo ""

# -------------------------------------------------
# Install
# -------------------------------------------------
install:
	pip install -e .

install-dev:
	pip install -e .[test]

# -------------------------------------------------
# Run
# -------------------------------------------------
run:
	uvicorn $(APP_NAME).main:app --reload --host 0.0.0.0 --port 8000

up:
	docker compose up --build

down:
	docker compose down

# -------------------------------------------------
# Code Quality
# -------------------------------------------------
format:
	black src
	ruff check src --fix

lint:
	ruff check src

typecheck:
	mypy src

test:
	pytest

test-all: format lint typecheck test

# -------------------------------------------------
# API Endpoint Helpers (CURL shortcuts)
# -------------------------------------------------
root:
	@echo "➡️  GET /"
	@curl -s $(HOST) | jq .

health:
	@echo "➡️  GET /api/v1/health"
	@curl -s $(API_V1)/health | jq .

echo:
	@echo "➡️  POST /api/v1/echo (valid)"
	@curl -s -X POST $(API_V1)/echo \
		-H "Content-Type: application/json" \
		-d '{"text": "hello from make"}' | jq .

echo-invalid:
	@echo "➡️  POST /api/v1/echo (invalid body)"
	@curl -s -X POST $(API_V1)/echo \
		-H "Content-Type: application/json" \
		-d '{}' | jq .

# -------------------------------------------------
# Clean
# -------------------------------------------------
clean:
	rm -rf .mypy_cache .ruff_cache .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
