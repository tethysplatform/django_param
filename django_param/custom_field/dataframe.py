# -*- coding: utf-8 -*-

from django import forms
from django_param.custom_widget.dataframewidget import DataFrameWidget


class DataFrameField(forms.Field):
    def __init__(self, *args, **kwargs):
        kwargs["widget"] = DataFrameWidget
        super().__init__(*args, **kwargs)

    def clean(self, value):
        """
        Validate the given value against all of self.fields, which is a
        list of Field instances.
        """
        super().clean(value)
        for field in self.fields:
            value = field.clean(value)
        return value
