============
Django_Param
============

django_param is a Django app to demonstrate using param with Django Form. For each question,
visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add 'datetimewidget', 'django_select2' and 'taggit'  to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'datetimewidget',
        'django_select2',
        'taggit',
    ]

2. Include the django_param URLconf in your project urls.py like this::

    path('django_param/', include('django_param.urls')),`

3. Run . test.sh to run test.