.PHONY: format lint test

export PYTHONPATH=.


all: format lint test

clean:
	find . -type f -name "*.py[co]" -delete -or -type d -name "__pycache__" -delete

format:
	black .

lint:
	flake8 --max-line-length=88 lib/ tests/

test:
	pytest -v
