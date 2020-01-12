venv:
	virtualenv -p /usr/bin/python3.6 .venv

init:
	pip install -r requirements.txt
