============
Django_Param
============

django_param is a Django app to demonstrate using param with Django Form. For each question,
visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "django_param" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_param',
    ]

2. Include the django_param URLconf in your project urls.py like this::

    path('django_param/', include('django_param.urls')),

3. Run ``python manage.py migrate`` to create the django_param.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a django_param (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/polls/ to use the django_param app.