.PHONY: clean
clean:
	@echo Cleaning generated code, build, docs, and distributables
	mvn clean
	cd docs && make clean
	rm -rf dist build


.PHONY: docs
docs:
	@echo Generating HTML docs. Note that this will use the installed
	@echo version of OCI, so you might want to run gen, build, and
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
	@echo Uninstalling then reinstalling OCI whl.
	pip uninstall -y oci || true
	pip install dist/oci-*.whl

.PHONY: release-test
release-test:
	@echo Uploading whl file to Test PyPI.
	@read -p "Press any key to continue: " -n 1 -r
	@echo
	pip install twine
	twine register dist/*.whl -r testpypi
	twine upload dist/* -r testpypi
	
.PHONY: release
release:
	@echo Uploading whl file to PyPI.
	@read -p "Press any key to continue: " -n 1 -r
	@echo
	pip install twine
	twine register dist/*.whl
	twine upload dist/*