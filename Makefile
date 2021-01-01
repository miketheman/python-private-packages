.DEFAULT_GOAL := test

PIPENV := $(shell command -v pipenv 2> /dev/null)

init:
ifndef PIPENV
	pip install pipenv
endif
	pipenv install --dev

clean:
	rm -fr .pytest_cache .coverage htmlcov/

test:
	pipenv run python -m pytest --black --pylint --cov=myawesomeapp

uninstall: clean
	pipenv --rm
