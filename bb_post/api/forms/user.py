from django import forms
from django.contrib.auth import authenticate

from bb_post.api.exceptions.user import UserBadCredentialsError


class CreateForm(forms.Form):

    email = forms.CharField()
    password = forms.CharField()

    def is_valid(self):
        super(CreateForm, self).is_valid()
        username = self.data.pop('email')
        password = self.data.pop('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                if not user.is_active:
                    raise UserBadCredentialsError('User is not activated')
            else:
                raise UserBadCredentialsError('User not found')
        else:
            raise UserBadCredentialsError('Provide both password and email')

        self.cleaned_data['user'] = user
        return True

