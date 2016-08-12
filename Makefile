.PHONY: docs
docs:
	@echo Generating HTML docs. Note that this will use the installed
	@echo version of OracleBMI, so you might want to run gen, build, and
	@echo install first.
	cd docs && make clean && sphinx-apidoc -o apidocs/ ../oraclebmi
	cd docs && make html
	@echo View the docs at docs/_build/html/index.html

.PHONY: test
test:
	@echo Running all tests that fit the pattern 'tests/test_*.py'
	python -m unittest discover

.PHONY: gen
gen:
	@echo Generating python APIs and Models.
	mvn clean install

.PHONY: build
build:
	@echo Creating whl file for distribution.
	python3 setup.py sdist
	python3 setup.py bdist_wheel

.PHONY: install
install:
	@echo Uninstalling then reinstalling OracleBMI whl.
	pip uninstall -y oraclebmi || true
	pip install dist/oraclebmi-*-py3-none-any.whl