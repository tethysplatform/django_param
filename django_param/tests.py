from django.test import TestCase

# Create your tests here.
import param
from django_param.forms import ParamForm
import django

django.setup()

from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class MyParam(param.Parameterized):
    probability = param.Number(0.5, bounds=(0,1), doc="Probability that...")
    test_string = param.String(default="test string", doc="Probability that...")


test_django_form_a = ContactForm({'subject': 'hello'})
# print(test_django_form_a)
test_param = MyParam()

# Test set data
# not self.bound and not self.initial:
no_bound_no_inital = ParamForm(param_class=test_param)

# Bound:
bound = ParamForm({'probability': 0.1, 'test_string': 'test_bound'}, param_class=test_param)

# Initial
initial = ParamForm(initial={'probability': 0.2, 'test_string': 'test_initial'}, param_class=test_param)

# Test using initial
with_bound_and_initial = ParamForm({'probability': 2, 'test_string': 'test'}, initial={'probability': 0.2}, param_class=test_param)
with_bound_and_initial.as_param()
with_bound_and_initial.errors
breakpoint()
