default:
	python3 setup.py sdist

egg:
	python3 setup.py bdist_egg

install:
	python3 setup.py install

uninstall:
	pip3 uninstall vcommand

clean:
	find `pwd` -name ".DS_Store" -delete
	find `pwd` -name "*.pyc" -delete
	find `pwd` -type d -name "__pycache__" -exec rm -rf {} \;
	find `pwd` -type d -name "__MACOSX" -exec rm -rf {} \;
	rm -rf ./build ./dist ./vcommand.egg-info

debug: uninstall default install
	@echo "[+] Debug..."