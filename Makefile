ifeq ($(OS), Windows_NT)

run: 
	python package/main.py

install: requirements.txt
	pip install -r requirements.txt

build: setup.py
	python setup.py build bdist_wheel

clean:
	if exist "./build" rd /s /q build
	if exist "./dist" rd /s /q dist
	if exist "./python_linked_list.egg-info" rd /s /q python_linked_list.egg-info
	
test:
	python tests/test_linked_list.py

else

run: 
	python3 package/main.py

install: requirements.txt
	pip3 install -r requirements.txt

build: setup.py
	python3 setup.py build bdist_wheel

clean:
	rm -rf build
	rm -rf dist
	rm -rf python_linked_list.egg-info

test:
	python3 tests/test_linked_list.py
	python3 tests/test_binary_tree.py

endif