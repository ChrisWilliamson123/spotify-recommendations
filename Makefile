all: requirements

env:
	virtualenv -p python3 env

requirements: env
	./env/bin/pip install -r ./etc/requirements.txt
