from django import forms
import param
from .widget_map import widget_map


class ParamForm(forms.Form):
    _param = None
    read_only = None
    _error_key_list = []
    cleaned_data = ""

    def __init__(self, *args, **kwargs):
        param_class = kwargs.pop('param', None)
        if param_class is None:
            raise KeyError('Keyword argument param is required.')
        if not isinstance(param_class, param.Parameterized):
            raise ValueError(f'{param_class} must be an instance of param.Parameterized.')
        self._param = param_class

        read_only = kwargs.pop('read_only', None)
        if read_only:
            self.read_only = read_only

        super().__init__(*args, **kwargs)
        self._generate_form_fields()

    @property
    def param(self):
        return self._param

    @property
    def widget(self):
        return widget_map

    def _add_error(self, key, message):
        # Only add error once for each parameter to avoid duplicate
        if key not in self._error_key_list:
            self._error_key_list.append(key)
            self.add_error(key, str(message))

    def _set_and_validate_data(self, data):
        for key, value in data.items():
            try:
                self.param.set_param(key, value)
            except ValueError as e:
                self._add_error(key, e)

    def _generate_form_fields(self):
        """
        Create a Django form from a Parameterized object.

        Returns:
            Form: a Django form with fields matching the parameters of the given parameterized object.
        """
        params = list(filter(lambda x: (x.precedence is None or x.precedence >= 0) and not x.constant,
                             self.param.params().values()))
        for p in sorted(params, key=lambda p: p.precedence or 9999):
            # TODO: Pass p.__dict__ as second argument instead of arbitrary
            p_name = p.name
            self.fields[p_name] = self.widget[type(p)](self.param, p, p.name)
            self.fields[p_name].label = p.name.capitalize()
            if self.read_only is None:
                widget_attribute = {'class': 'form-control'}
            else:
                # TODO: Should this be readonly instead of disable?
                widget_attribute = {'class': 'form-control', 'disabled': self.read_only}
            self.fields[p_name].widget.attrs.update(widget_attribute)
        # self.fields = self.base_fields

    def as_param(self):
        self.clean()
        return self.param

    def clean(self):
        self.cleaned_data = super().clean()
        # Use bound data to set the value if we both have bound and initial data.
        if self.is_bound and self.initial:
            self._set_and_validate_data(self.data)
            return
        else:
            # Set values according to bound data
            if self.is_bound:
                self._set_and_validate_data(self.data)
                return
            # Set values according to initial data
            if self.initial:
                self._set_and_validate_data(self.initial)
                return
