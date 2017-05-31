Python 3 + Selene + Docker Tutorial
===================================
Author: Sergey Pirogov
blog: http://automation-remarks.com

Requirements: 
-------------

- Python 3
- Docker
- Git

Create project:
---------------

```
mkdir selene_demo
```

Start SUT using **docker** and **docker-compose**:

1) Download docker-compose.yml file

```
curl -O https://raw.githubusercontent.com/SergeyPirogov/python-video-service/master/docker-compose.yml
```

2) Start application
 
```
docker-compose up -d
```

3) Check application started at http://localhost:8086

Install pipenv:
---------------

Pipenv docs: https://github.com/kennethreitz/pipenv

```
pip install pipenv
```

Create project virtualenv with python 3 installed:
--------------------------------------------------

```
pipenv --three
```

Activate virtualenv:
--------------------

```
pipenv shell
```

Required packages:
------------------

- selene
- pytest
- pytest-allure-adapter
- pytest-env
- testcontainers

Install Selene:

Latest alfa release:

```
pip install selene --pre
```

Latest development:

```
pip install git+https://github.com/yashaka/selene.git
```

Install pytest:

```
pip install pytest
```

Install pytest-env:

```
pip install pytest-env
```

**Open project in Pycharm**

Create python packages **src** and **tests**.
    
Under **src** create python module package **pages**

Create file **pytest.ini**:
    
```
[pytest]
addopts = --tb=short -sv
env =
    selene_browser_name=chrome
    selene_base_url=http://localhost:8086    
```
    
Start creation of page object modules under under **pages** package:

- login_page.py
- main_page.py

Describe page objects

Run tests in console:

```
pytest -sv tests/ 
```

You can specify env variables:

```
selene_browser_name=chrome pytest -sv tests/
```

Install testcontainers:
-----------------------

https://github.com/SergeyPirogov/testcontainers-python

Release version:

```
pip install testcontainers
```

Development version:

```
pip install git+https://github.com/SergeyPirogov/testcontainers-python.git
```
Install Allure adaptor:

```
pip install pytest-allure-adaptor
```

Install [Allure command line](http://wiki.qatools.ru/display/AL/Allure+Commandline)


Install allure2:

```
pip install git+https://github.com/allure-framework/allure-python2.git@master#subdirectory=allure-python-commons
pip install git+https://github.com/allure-framework/allure-python2.git@master#subdirectory=allure-pytest
```

Create run.sh in case of allure2:
--------------

```
#!/bin/bash
rm -rf report

mkdir -p report

rm -rf allure-report

pytest tests --alluredir=report

allure_gen/bin/allure generate report
```

Run tests:

```
./run.sh
```

Travis integration

