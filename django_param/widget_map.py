"""
********************************************************************************
* Name: param_widgets.py
* Author: Scott Christensen and Nathan Swain
* Created On: January 18, 2019
* Copyright: (c) Aquaveo 2019
********************************************************************************
"""
import param
from django import forms
from django_select2.forms import Select2Widget
from django.forms.widgets import NumberInput, CheckboxInput, SelectMultiple, Textarea, TextInput, Select,\
    ClearableFileInput
from colorfield.fields import ColorWidget
from django_param.custom_field.dataframe import DataFrameField
from django_param.custom_widget.dataframewidget import DataFrameWidget
from django_param.custom_widget.datepicker_widget import DatePickerWidget

widget_map = {
    param.Foldername:
        lambda po, p, name: forms.FilePathField(
            initial=po.inspect_value(name) or p.default,
            path=p.search_paths,
            widget=Select,
        ),
    param.Boolean:
        lambda po, p, name: forms.BooleanField(
            initial=po.inspect_value(name) or p.default,
            required=False,
            widget=CheckboxInput,
        ),
    # param.Array: ,
    # param.Dynamic: ,
    param.Filename:
        lambda po, p, name: forms.FileField(
            initial=po.inspect_value(name) or p.default,
            widget=ClearableFileInput,
        ),
    param.Dict:
        lambda po, p, name: forms.CharField(
            initial=po.inspect_value(name) or p.default,
            widget_map=TextInput,
        ),
    param.XYCoordinates:
        lambda po, p, name: forms.CharField(
            initial=po.inspect_value(name) or p.default,
            widget=TextInput,
        ),
    param.Selector:
        lambda po, p, name: forms.ChoiceField(
            initial=po.inspect_value(name) or p.default,
            widget=Select,
        ),
    # param.HookList,
    # param.Action: ,
    param.parameterized.String:
        lambda po, p, name: forms.CharField(
            initial=po.inspect_value(name) or p.default,
            widget=Textarea,
        ),
    param.Magnitude:
        lambda po, p, name: forms.FloatField(
            initial=po.inspect_value(name) or p.default,
            widget=NumberInput(attrs={'step': 0.01, 'max': 1.0, 'min': 0.0}),
        ),
    # param.Composite,
    param.Color:
        lambda po, p, name: forms.CharField(
            initial=po.inspect_value(name) or p.default,
            widget=ColorWidget,
        ),
    param.ObjectSelector:
        lambda po, p, name: forms.ChoiceField(
            initial=po.inspect_value(name) or p.default,
            widget=Select2Widget,
            choices=p.get_range().items(),
        ),
    param.Number:
        lambda po, p, name: forms.FloatField(
            initial=po.inspect_value(name) or p.default,
            widget=NumberInput(attrs={'step': 0.01, 'max': p.bounds[1], 'min': p.bounds[0]}),
        ),
    param.Range:
        lambda po, p, name: forms.MultiValueField(
            initial=po.inspect_value(name) or p.default,
            widget=TextInput,
        ),
    param.NumericTuple:
        lambda po, p, name: forms.MultiValueField(
            initial=po.inspect_value(name) or p.default,
            widget=TextInput,
        ),
    param.Date:
        lambda po, p, name: forms.DateTimeField(
            initial=po.inspect_value(name).strftime('%m-%d-%Y') or p.default.strftime('%m-%d-%Y'),
            widget=DatePickerWidget(
                attrs={
                    'minDate': p.bounds[0].strftime(
                        '%m-%d-%Y') if p.bounds else '0000-01-01',  # start of supported time
                    'maxDate': p.bounds[1].strftime(
                        '%m-%d-%Y') if p.bounds else '9999-12-31',  # end of supported time
                    'format': 'm-d-Y',
                    'formatDate': 'm-d-Y',
                    'timepicker': 'false',
                },
            ),
        ),
    param.List:
        lambda po, p, name: forms.MultipleChoiceField(
            # initial=po.inspect_value(name) or p.default,
            choices=((x, x) for x in po.inspect_value(name)),
            widget=SelectMultiple,
        ),
    param.Path:
        lambda po, p, name: forms.FilePathField(
            initial=po.inspect_value(name) or p.default,
            path=p.search_paths,
            widget=Select,
        ),
    param.MultiFileSelector:
        lambda po, p, name: forms.MultipleChoiceField(
            # initial=po.inspect_value(name) or p.default,
            choices=((x, x) for x in po.inspect_value(name)),
            widget=SelectMultiple,
        ),
    param.ClassSelector:
        lambda po, p, name: forms.ChoiceField(
            initial=po.inspect_value(name) or p.default,
            widget=Select,
        ),
    param.FileSelector:
        lambda po, p, name: forms.ChoiceField(
            choices=((x, x) for x in po.inspect_value(name)),
            widget=Select,
        ),
    param.ListSelector:
        lambda po, p, name: forms.MultipleChoiceField(
            choices=((x, x) for x in po.inspect_value(name)),
            widget=SelectMultiple,
        ),
    # param.Callable,
    param.Tuple:
        lambda po, p, name: forms.MultiValueField(
            initial=po.inspect_value(name) or p.default,
            widget=TextInput,
        ),
    param.Integer:
        lambda po, p, name: forms.IntegerField(
            initial=po.inspect_value(name) or p.default,
            widget=NumberInput,
        ),
    param.DataFrame:
        lambda po, p, name: DataFrameField(
            initial=po.dataframe,
            widget=DataFrameWidget(),
        )
}
