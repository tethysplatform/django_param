[<img src="https://coveralls.io/repos/github/tethysplatform/django_param/badge.svg">](https://coveralls.io/github/tethysplatform/django_param)

# Django Param

Django Param provides the ParamForm class which translates a param class into a native Django Form.

## Quick start

Add 'colorfield', 'django_select2', 'django_param' and 'django.forms' to your INSTALLED_APPS setting like this:

    ```python
    INSTALLED_APPS = [
        ...
        'colorfield',
        'django_select2',
        'django_param',
    ]
    ```


## Usage

```python
# Specify your param class
class MyParam(param.Parameterized):
    probability = param.Number(0.5, bounds=(0, 1), doc="Probability that...")
    test_string = param.String(default="test string", doc="Your String")

my_param = MyParam()

# Initialize Django Form
form = ParamForm({'probability': 0.1, 'test_string': 'test_bound'}, param=my_param)

# Get data from request.POST
form = ParamForm(request.POST, param=my_param)

# To return param with values from request.POST
param = form.as_param()
```

Use form in template like a normal Django form:

- First you need to add the form media, you can include `{{ form.media }}` in the head element of your page.
- To add the form, simply use `{{ form }}`

## Supported param.Parameters

- Boolean
- Color
- CalendarDate
- DataFrame
- Date
- FileSelector
- ListSelector
- Magnitude
- MultiFileSelector
- NumericTuple
- ObjectSelector
- Range
- Selector
- String
- Tuple
- XYCoordinates

## Custom Widgets

You can also override any default widget with your own custom widgets. For example:

```python
widget_map = {
    param.String:
        lambda parameterized_object, parameter, name: forms.CharField(
            initial=parameterized_object.inspect_value(name) or parameter.default,
            widget=Textarea,
        ),
}

form = ParamForm(param=my_param, widget_map=widget_map)
```