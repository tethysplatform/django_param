from django import forms


class DatePickerWidget(forms.Widget):
    template_name = 'django_param/datepicker/datepicker.html'

    class Media:
        css = {'all': ('django_param/datepicker/jquery.datetimepicker.min.css',)}
        js = [
            'django_param/datepicker/jquery.datetimepicker.full.js',
        ]

    def get_context(self, name, value, attrs):
        context = {}
        context['widget'] = {
            'name': name,
            'is_hidden': self.is_hidden,
            'required': self.is_required,
            'value': self.format_value(value),
            'attrs': self.build_attrs(self.attrs, attrs),
            'template_name': self.template_name,
        }
        return context
