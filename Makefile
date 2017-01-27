.PHONY: clean
clean:
	@echo Cleaning generated code, build, docs, and distributables
	mvn clean
	cd docs && make clean
	rm -rf dist build


.PHONY: docs
docs:
	@echo Generating HTML docs. Note that this will use the installed
	@echo version of OracleBMC, so you might want to run gen, build, and
	@echo install first.
	cd docs && make html
	@echo View the docs at docs/_build/html/index.html


.PHONY: test
test:
	@echo Running all tox environments
	tox


.PHONY: gen
gen:
	@echo Generating python APIs and Models.
	mvn clean install


.PHONY: build
build:
	@echo Creating .tar.gz, .whl files for distribution.
	python setup.py sdist bdist_wheel
	@echo Creating .zip for distribution.
	python scripts/zip-wheel


.PHONY: install
install:
	@echo Uninstalling then reinstalling OracleBMC whl.
	pip uninstall -y oraclebmc || true
	pip install dist/oraclebmc-*-py3-none-any.whl