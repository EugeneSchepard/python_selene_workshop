pipenv --three
pipenv shell
pipenv install pytest
pipenv install pytest-env
pipenv run pip install git+https://github.com/yashaka/selene.git
pipenv run pip install git+https://github.com/SergeyPirogov/testcontainers-python.git
pipenv run pip install git+https://github.com/allure-framework/allure-python2.git@master#subdirectory=allure-python-commons
pipenv run pip install git+https://github.com/allure-framework/allure-python2.git@master#subdirectory=allure-pytest