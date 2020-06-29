from django.test import TestCase

# Create your tests here.
import param
from django_param.forms import ParamForm
import django

django.setup()


class MyParam(param.Parameterized):
    a = param.Number(0.5,bounds=(0,1),doc="Probability that...")
    b = param.Boolean(False,doc="Enable feature...")


class MyParama(param.Parameterized):
    c = param.Number(0.3,bounds=(0,1),doc="Probability that...")
    d = param.Boolean(False,doc="Enable feature...")


test_param = MyParam()
test_django_form_a = ParamForm(test_param)
print(test_django_form_a)
test_param = MyParama()
test_django_form_b = ParamForm(test_param)
print(test_django_form_b)