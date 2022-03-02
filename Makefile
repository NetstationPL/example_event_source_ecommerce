test:
	pytest es_ecommerce/product-catalog
	pytest es_ecommerce/pricing
	cd django_application;python manage.py test
