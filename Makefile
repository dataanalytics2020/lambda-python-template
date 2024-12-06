.PHONY: install test lint format clean

install:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

test:
	pytest --cov=src tests/ --cov-report=term-missing

lint:
	flake8 src tests
	mypy src tests
	black --check src tests

format:
	black src tests

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".coverage" -exec rm -rf {} +
	find . -type d -name "htmlcov" -exec rm -rf {} + 