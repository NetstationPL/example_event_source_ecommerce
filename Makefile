test:
	pytest ecommerce/product-catalog
	pytest ecommerce/pricing
	cd django_application;python manage.py test
