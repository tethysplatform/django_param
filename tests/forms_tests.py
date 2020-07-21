import param
from django_param.forms import ParamForm
import pytest


class MyParam(param.Parameterized):
    probability = param.Number(0.5, bounds=(0, 1), doc="Probability that...")
    test_string = param.String(default="test string", doc="Probability that...")


class TestForm:
    def test_form_empty(self):
        with pytest.raises(KeyError, match="Keyword argument param is required."):
            ParamForm()

    def test_form_invalid_param(self):
        with pytest.raises(ValueError, match="test must be an instance of param.Parameterized."):
            ParamForm(param="test")

    def test_form_no_bound(self):
        test_param = MyParam()

        # Test read-only
        no_bound_no_initial = ParamForm(param=test_param, read_only=True)
        no_bound_no_initial.clean()
        expected_html = '<tr><th><label for="id_probability">Probability:</label></th><td><input type="number"' \
                        ' name="probability" value="0.5" step="0.01" max="1" min="0" class="form-control" disabled' \
                        ' required id="id_probability"></td></tr>\n<tr><th><label for="id_test_string">' \
                        'Test_string:</label></th><td><textarea name="test_string" cols="40" rows="10"' \
                        ' class="form-control" disabled required id="id_test_string">\ntest string</textarea></td></tr>'
        # Check results. No bound has no data for validation so is_valid is false
        assert str(no_bound_no_initial) == expected_html
        assert no_bound_no_initial.is_bound is False
        assert no_bound_no_initial.is_valid() is False
        assert no_bound_no_initial.errors == {}

    def test_form_initial(self):
        test_param = MyParam()

        initial = ParamForm(initial={'probability': 0.2, 'test_string': 'test_initial'}, param=test_param)
        initial.clean()
        expected_html = '<tr><th><label for="id_probability">Probability:</label></th><td><input type="number"' \
                        ' name="probability" value="0.2" step="0.01" max="1" min="0" class="form-control"' \
                        ' required id="id_probability"></td></tr>\n<tr><th><label for="id_test_string">Test_string:' \
                        '</label></th><td><textarea name="test_string" cols="40" rows="10" class="form-control"' \
                        ' required id="id_test_string">\ntest_initial</textarea></td></tr>'

        # Check results. No bound has no data for validation so is_valid is false
        assert str(initial) == expected_html
        assert initial.is_bound is False
        assert initial.is_valid() is False
        assert initial.errors == {}

        # Check param new initial value
        assert initial.as_param().probability == 0.2
        assert initial.as_param().test_string == "test_initial"

    def test_form_bound(self):
        test_param = MyParam()

        # Bound:
        bound = ParamForm({'probability': 0.1, 'test_string': 'test_bound'}, param=test_param)
        expected_html = '<tr><th><label for="id_probability">Probability:</label></th><td><input type="number"' \
                        ' name="probability" value="0.1" step="0.01" max="1" min="0" class="form-control"' \
                        ' required id="id_probability"></td></tr>\n<tr><th><label for="id_test_string">' \
                        'Test_string:</label></th><td><textarea name="test_string" cols="40" rows="10"' \
                        ' class="form-control" required id="id_test_string">\ntest_bound</textarea></td></tr>'

        # Check results
        assert str(bound) == expected_html
        assert bound.is_bound is True
        assert bound.is_valid() is True

    def test_changed_form(self):
        test_param = MyParam()
        # Bound and with initial. It should use the bound data and return errors:
        data = {'probability': 0.2, 'test_string': 'test'}
        data_new = {'probability': 0.8, 'test_string': 'new string'}
        form = ParamForm(data, initial=data, param=test_param)
        form.clean()
        # Check if form has changed
        assert form.has_changed() is False
        assert form.as_param().probability == 0.2
        assert form.as_param().test_string == 'test'

        # Change form
        form = ParamForm(data_new, initial=data, param=test_param)

        # Check results
        assert form.is_bound is True
        assert form.is_valid() is True
        assert form.has_changed() is True
        assert form.as_param().probability == 0.8
        assert form.as_param().test_string == 'new string'

    def test_invalid_form_bound(self):
        test_param = MyParam()
        # Bound and with initial. It should use the bound data and return errors:
        bound_error = ParamForm({'probability': 2, 'test_string': 'test'}, initial={'probability': 0.2},
                                param=test_param)
        bound_error.clean()
        error_message = {'probability': ["Parameter 'probability' must be at most 1"]}
        # Check results
        assert bound_error.is_bound is True
        assert bound_error.is_valid() is False
        assert bound_error.errors == error_message

    def test_prefix(self):
        test_param = MyParam()
        expected_html = '<tr><th><label for="id_prefix-probability">Probability:</label></th><td><input type="number"' \
                        ' name="prefix-probability" value="0.5" step="0.01" max="1" min="0" class="form-control"' \
                        ' required id="id_prefix-probability"></td></tr>\n<tr><th><label for="id_prefix-test_string">' \
                        'Test_string:</label></th><td><textarea name="prefix-test_string" cols="40" rows="10"' \
                        ' class="form-control" required id="id_prefix-test_string">\ntest string</textarea></td></tr>'

        # Check results
        form = ParamForm(param=test_param, prefix="prefix")
        assert form.is_bound is False
        assert str(form) == expected_html
