from allauth.account.forms import LoginForm, SignupForm


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)

        self.fields['login'].widget.attrs['placeholder'] = ''
        self.fields['password'].widget.attrs['placeholder'] = ''


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = ''
        self.fields['email'].label = 'メールアドレス'
        self.fields['email'].widget.attrs['placeholder'] = ''
        self.fields['password1'].widget.attrs['placeholder'] = ''
        self.fields['password2'].widget.attrs['placeholder'] = ''
