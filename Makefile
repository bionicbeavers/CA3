install:
	pip install --upgrade pip&\
	pip install -r requirements.txt
lint:
	pylint --disable=C,R calculator.py
test:
	python -m pytest -vv --cov=calculator test_calculator.py