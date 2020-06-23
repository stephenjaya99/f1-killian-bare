install:
	pipenv install --dev
	pipenv run python manage.py migrate
	pipenv run python manage.py collectstatic
	pipenv run python manage.py createsuperuser
	pipenv run pre-commit install
