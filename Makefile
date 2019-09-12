default:
	python setup.py sdist

egg:
	python setup.py bdist_egg

install:
	python setup.py install

uninstall:
	pip uninstall vcommand

clean:
	find `pwd` -name ".DS_Store" -delete
	find `pwd` -name "*.pyc" -delete
	find `pwd` -type d -name "__pycache__" -exec rm -rf {} \;
	find `pwd` -type d -name "__MACOSX" -exec rm -rf {} \;
	rm -rf ./build ./dist ./vcommand.egg-info

debug: uninstall default install
	@echo "[+] Debug..."