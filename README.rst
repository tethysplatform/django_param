============
Django_Param
============
.. image:: https://coveralls.io/repos/github/Aquaveo/django_param/badge.svg

:target: https://coveralls.io/github/Aquaveo/django_param

django_param provides ParamForm class which allows python param to be used in django form.

Quick start
-----------

1. Add 'datetimewidget', 'django_select2' and 'taggit'  to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'datetimewidget',
        'django_select2',
        'taggit',
    ]


2. Usage:

.. code-block:: python

    # Specify your param class
    class MyParam(param.Parameterized):
        probability = param.Number(0.5, bounds=(0, 1), doc="Probability that...")
        test_string = param.String(default="test string", doc="Your String")

    my_param = MyParam()

    # Initialize Django Form
    django_bound_form = ParamForm({'probability': 0.1, 'test_string': 'test_bound'}, param_class=my_param)