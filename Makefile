.PHONY: format lint test

export PYTHONPATH=.


all: format lint test

format:
	black .

lint:
	flake8 --max-line-length=88 lib/ tests/

test:
	pytest -v
