from django import forms
from .models import UserClient
from django.core.exceptions import ObjectDoesNotExist


class ClientCreateForm(forms.Form):
    def clean_client_name(self):
        client_name = self.cleaned_data['client_name']
        try:
            UserClient.objects.get(client_name=client_name)
        except ObjectDoesNotExist:
            return client_name
        data = 'Người dùng ' + client_name + ' đã tồn tại!'
        raise forms.ValidationError(data)

    class Meta:
        model = UserClient
        fields = '__all__'
