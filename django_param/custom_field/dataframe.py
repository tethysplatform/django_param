# -*- coding: utf-8 -*-

from django import forms
from django_param.custom_widget.dataframewidget import DataFrameWidget


class DataFrameField(forms.Field):
    def __init__(self, *args, **kwargs):
        kwargs["widget"] = DataFrameWidget
        super().__init__(*args, **kwargs)
