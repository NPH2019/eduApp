from django import forms


class LoginForm(forms.Form):
    class Meta:
        fields = ('username', 'password')

    username = forms.CharField(
        label='Tài khoản', min_length=4, max_length=150, required=True,
        error_messages={
            'required': 'Vui lòng nhập tài khoản'
        },
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autofocus': 'true',
                'parsley-trigger': 'change',
                'placeholder': 'Tên đăng nhập'
            }
        )
    )

    password = forms.CharField(
        label='Mật khẩu', min_length=4, max_length=20, required=True,
        error_messages={
            'required': 'Vui lòng nhập mật khẩu'
        },
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'autofocus': 'true',
                'parsley-trigger': 'change',
                'placeholder': 'Mật khẩu'
            }
        )
    )