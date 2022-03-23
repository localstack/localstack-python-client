VENV_DIR ?= .venv
VENV_RUN = . $(VENV_DIR)/bin/activate
PIP_CMD ?= pip
BUILD_DIR ?= dist

usage:             ## Show this help
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

install:           ## Install dependencies in local virtualenv folder
	(test `which virtualenv` || $(PIP_CMD) install --user virtualenv) && \
		(test -e $(VENV_DIR) || virtualenv $(VENV_OPTS) $(VENV_DIR)) && \
		($(VENV_RUN) && $(PIP_CMD) install --upgrade pip) && \
		(test ! -e setup.cfg || ($(VENV_RUN); $(PIP_CMD) install .[test]))

publish:           ## Publish the library to the central PyPi repository
	# build and upload archive
	($(VENV_RUN); ./setup.py sdist && twine upload $(BUILD_DIR)/*.tar.gz)

test:              ## Run automated tests
	($(VENV_RUN); test `which localstack` || pip install .[test]) && \
	$(VENV_RUN); DEBUG=$(DEBUG) PYTHONPATH=`pwd` nosetests --with-coverage --logging-level=WARNING --nocapture --no-skip --exe --cover-erase --cover-tests --cover-inclusive --cover-package=localstack_client --with-xunit --exclude='$(VENV_DIR).*' .

lint:              ## Run code linter to check code style
	($(VENV_RUN); pycodestyle --max-line-length=100 --ignore=E128 --exclude=node_modules,legacy,$(VENV_DIR),dist .)

clean:             ## Clean up virtualenv
	rm -rf $(VENV_DIR)

.PHONY: usage install clean publish test lint
