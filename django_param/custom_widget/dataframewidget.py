from django import forms


class DataFrameWidget(forms.Widget):
    template_name = 'django_param/dataframe/dataframe.html'

    class Media:
        css = {'all': ('django_param/dataframe/dataframe.css',)}
        js = [
            'django_param/dataframe/dataframe.js',
        ]

    def get_context(self, name, value, attrs):
        context = {}
        # Get columns
        columns = [col for col in value.columns]
        row_values = value.values.tolist()
        # Get rows
        rows = list()
        for row_value in row_values:
            rows.append(dict(zip(columns, row_value)))

        context['widget'] = {
            'name': name,
            'is_hidden': self.is_hidden,
            'required': self.is_required,
            'value': value.to_html(),
            'columns': columns,
            'rows': rows,
            'attrs': self.build_attrs(self.attrs, attrs),
            'template_name': self.template_name,
        }
        return context
