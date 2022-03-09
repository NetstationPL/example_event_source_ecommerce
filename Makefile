install:
	poetry install
	poetry shell
	cd django_application;python manage.py makemigrations;python manage.py migrate;echo "Create superuser to admin panel:\n";python manage.py createsuperuser;
test:
	poetry shell
	pytest ecommerce/product-catalog
	pytest ecommerce/pricing
	pytest ecommerce/taxes
	pytest ecommerce/crm
	pytest ecommerce/ordering
	pytest infra
	cd django_application;python manage.py test

run:
	poetry shell
	cd django_application;python manage.py runserver
