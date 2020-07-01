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
from datetimewidget.widgets import DateWidget
from django_select2.forms import Select2Widget
from taggit.forms import TagField
from django.forms.widgets import NumberInput, CheckboxInput, SelectMultiple, Textarea, TextInput, Select,\
    ClearableFileInput


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
        lambda po, p, name: forms.MultiValueField(
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
            widget=NumberInput,
        ),
    # param.Composite,
    param.Color:
        lambda po, p, name: forms.CharField(
            initial=po.inspect_value(name) or p.default,
            widget=TextInput,
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
            widget=NumberInput,
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
            initial=po.inspect_value(name) or p.default,
            widget=DateWidget(
                options={
                    'startDate': p.bounds[0].strftime(
                        '%Y-%m-%d') if p.bounds else '0000-01-01',  # start of supported time
                    'endDate': p.bounds[1].strftime(
                        '%Y-%m-%d') if p.bounds else '9999-12-31',  # end of supported time
                    'format': 'mm/dd/yyyy',
                    'autoclose': True,
                    # 'showMeridian': False,
                    'minView': 2,  # month view
                    'maxView': 4,  # 10-year overview
                    'todayBtn': 'true',
                    'clearBtn': True,
                    'todayHighlight': True,
                    'minuteStep': 5,
                    'pickerPosition': 'bottom-left',
                    'forceParse': 'true',
                    'keyboardNavigation': 'true',
                },
                bootstrap_version=3
            ),
        ),
    param.List:
        lambda po, p, name: TagField(
            initial=po.inspect_value(name) or p.default,
        ),
    param.Path:
        lambda po, p, name: forms.FilePathField(
            initial=po.inspect_value(name) or p.default,
            path=p.search_paths,
            widget=Select,
        ),
    param.MultiFileSelector:
        lambda po, p, name: forms.MultipleChoiceField(
            initial=po.inspect_value(name) or p.default,
            widget=SelectMultiple,
        ),
    param.ClassSelector:
        lambda po, p, name: forms.ChoiceField(
            initial=po.inspect_value(name) or p.default,
            widget=Select,
        ),
    param.FileSelector:
        lambda po, p, name: forms.ChoiceField(
            initial=po.inspect_value(name) or p.default,
            widget=Select,
        ),
    param.ListSelector:
        lambda po, p, name: forms.MultipleChoiceField(
            initial=po.inspect_value(name) or p.default,
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
    # TODO: Implement DataFrameField someday...
    # param.DataFrame:
    #     lambda po, p, name: DataFrameField(
    #         initial=po.inspect_value(name) is not None or p.default is not None
    #     )
}
