test:
	pytest ecommerce/product-catalog
	pytest ecommerce/pricing
	pytest ecommerce/taxes
	pytest ecommerce/crm
	pytest infra
	cd django_application;python manage.py test
