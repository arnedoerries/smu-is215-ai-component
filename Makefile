.PHONY: run dev install lint test help

help:
	@echo "Available commands:"
	@echo "  make run                    - Start FastAPI development server"
	@echo "  make install                - Install dependencies"
	@echo "  make update-requirements    - Update requirements.txt from code (for development purposes)"

run:
	fastapi dev

install:
	pip install -r requirements.txt

update-requirements:
	pip freeze > requirements.txt
