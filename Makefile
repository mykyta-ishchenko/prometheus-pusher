.PHONY: lint fix python-version env version name name-version

NAME := $(shell grep -E '^name = "([^"]+)"' pyproject.toml | head -n1 | awk -F'"' '{print $$2}')
VERSION := $(shell grep -E '^version = "([^"]+)"' pyproject.toml | head -n1 | awk -F'"' '{print $$2}')
PYTHON := $(shell grep -E 'python = "([^"]+)"' pyproject.toml | awk -F'"' '{print $$2}' | sed 's/^\^//')

lint:
	@echo "Running linters..."
	poetry run ruff format .
	poetry run ruff check .

fix:
	@echo "Running linters with auto-fix..."
	poetry run ruff format .
	poetry run ruff check --fix .

python-version:
	@echo $(PYTHON)

env:
	@echo "set -o allexport; source .env; set +o allexport"

version:
	@echo $(VERSION)

name:
	@echo "$(NAME)"

name-version:
	@echo "$(VERSION):$(NAME)"
