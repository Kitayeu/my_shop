My_shop
================================

### This is online shop

### Implemented:
* celery for asynchronous task, use RabbitMQ
* sending emails
* export as a csv, generate pdf files
* search using trigrams
* authentication Django, logging via Facebook and Google
* REST API based on Django Rest Framework
* documentation from Rest Framework
* Swagger
* database PostgreSQL

### Getting Started:
1. use yourself data for email, facebook, google from settings.py
2. enable access of insecure applications in mail
3. RabbitMQ Command Prompt run:    rabbitmq-service.bat start
4. to view process manager   http://localhost:15672/
5. in terminal run:   celery -A my_shop worker -l info -P gevent
6. in terminal to run server: python manage.py runserver_plus --cert-file cert.crt
7. use address to connect: https://mysite.com:8000/

### Additional Programs:
- RabbitMQ 3.9.7
- Erlang 23.3
- PostgreSQL 11

## Required packages:

* Python 3.9
* virtualenv + pip
* Git