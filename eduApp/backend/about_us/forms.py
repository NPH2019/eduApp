from django import forms
from .models import About


class AboutForm(forms.Form):
    class Meta:
        model = About
        fields = '__all__'



# from django import forms
#
#
# class AboutForm(forms.Form):
#     class Meta:
#         fields = ('about_description')
#
#     about_description = forms.CharField(
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'form-control form-control-sm s-input-form',
#                 'rows': '2',
#                 'parsley-trigger': 'change',
#             }
#         )
#     )


