from django.forms import Form
import param
from .widget_map import widget_map


class ParamForm(Form):
    _param = None
    form_field_prefix = None
    read_only = None

    def __init__(self, p=None, *args, **kwargs):
        if not isinstance(p, param.Parameterized):
            raise ValueError
        self._param = p
        super().__init__(*args, **kwargs)
        self._generate_form_fields()

    @property
    def param(self):
        return self._param

    def _generate_form_fields(self, set_options=None):
        """
        Create a Django form from a Parameterized object.

        Args:
            parameterized_obj(Parameterized): the parameterized object.
            set_options(dict<attrib_name, initial_value>): Dictionary of initial value for one or more fields.
            form_field_prefix(str): A prefix to prepend to form fields
        Returns:
            Form: a Django form with fields matching the parameters of the given parameterized object.
        """
        params = list(filter(lambda x: (x.precedence is None or x.precedence >= 0) and not x.constant,
                             self.param.params().values()))
        for p in sorted(params, key=lambda p: p.precedence or 9999):
            # TODO: Pass p.__dict__ as second argument instead of arbitrary
            p_name = p.name
            if self.form_field_prefix is not None:
                p_name = self.form_field_prefix + p_name
            self.fields[p_name] = widget_map[type(p)](self.param, p, p.name)
            self.fields[p_name].label = p.name.capitalize()
            self.fields[p_name].widget.attrs.update({'class': 'form-control', 'disabled': self.read_only})
        # self.fields = self.base_fields

# my_param_form = ParamForm(param=MyParam)
