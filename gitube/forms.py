from django.forms import ModelForm

class BaseModelForm(ModelForm):
    def as_table(self):
        "Returns this form rendered as HTML <tr>s -- excluding the <table></table>."
        return self._html_output(
            normal_row = u'<tr%(html_class_attr)s><th>%(label)s</th><td>%(field)s%(help_text)s%(errors)s</td></tr>',
            error_row = u'<tr><td colspan="2">%s</td></tr>',
            row_ender = u'</td></tr>',
            help_text_html = u'<br />%s',
            errors_on_separate_row = False)
    
