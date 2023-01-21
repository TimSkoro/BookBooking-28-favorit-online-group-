create-superuser:
	python manage.py createsuperuser --username=$(shell cat .env | grep DJANGO_SU_NAME | cut -d '=' -f2) --email=$(shell cat .env | grep DJANGO_SU_EMAIL | cut -d '=' -f2)