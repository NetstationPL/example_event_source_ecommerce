test:
	pytest ecommerce/product-catalog
	pytest ecommerce/pricing
	pytest ecommerce/taxes
	cd django_application;python manage.py test
