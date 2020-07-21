============
Django_Param
============
.. image:: https://coveralls.io/repos/github/Aquaveo/django_param/badge.svg

:target: https://coveralls.io/github/Aquaveo/django_param

django_param provides ParamForm class which allows python param to be used in django form.

Quick start
-----------

1. Add 'django_select2' and 'django_param'  to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_select2',
        'django_param',
    ]


2. Usage:

.. code-block:: python

    # Specify your param class
    class MyParam(param.Parameterized):
        probability = param.Number(0.5, bounds=(0, 1), doc="Probability that...")
        test_string = param.String(default="test string", doc="Your String")

    my_param = MyParam()

    # Initialize Django Form
    django_bound_form = ParamForm({'probability': 0.1, 'test_string': 'test_bound'}, param=my_param)

3. Add Form data (assuming your form is named form):

- First you need to add the form media, you can include {{ form.media }} in your header page.
- To add the form, simply use {{ form }}

4. Supported Param Class:

- Boolean - param.Boolean(True, doc="A sample Boolean parameter")
- Color Picker - param.Color(default='#FFFFFF')
- Dataframe (Pandas) - param.DataFrame(pd.util.testing.makeDataFrame().iloc[:3])
- Date - param.Date(dt.datetime(2017, 1, 1), bounds=(dt.datetime(2017, 1, 1), dt.datetime(2017, 2, 1)))
- List - param.List(default=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
- Magnitude - param.Magnitude(default=0.9)
- Multiple Files - param.MultiFileSelector(path='*', precedence=0.5)
- Number - param.Number(49, bounds=(0, 100), doc="Any Number between 0 to 100")
- Select String - select_string = param.ObjectSelector(default="yellow", objects=["red", "yellow", "green"])
- String - param.String(default="hello world!", doc="Your String")
- XY Coordinates - param.XYCoordinates(default=(-111.65, 40.23))
