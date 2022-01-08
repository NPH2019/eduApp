from django import forms
from django.core.exceptions import ObjectDoesNotExist

from .models import Program


class ProgramCreateForm(forms.Form):
    def clean_cash_code(self):
        program_abbreviations = self.cleaned_data['program_abbreviations']
        try:
            Program.objects.get(program_abbreviations=program_abbreviations)
        except ObjectDoesNotExist:
            return program_abbreviations
        data = 'Chương trình ' + program_abbreviations + ' đã tồn tại!'
        raise forms.ValidationError(data)

    class Meta:
        model = Program
        fields = '__all__'
