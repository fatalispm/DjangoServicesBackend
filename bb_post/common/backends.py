from django.contrib.auth import get_user_model

from bb_post.api.exceptions.user import AuthenticationFailed
from bb_post.models.token import Token


class EmailBackend:
    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if getattr(user, 'is_active', False) and user.check_password(
                    password):
                return user


def get_authorization_header(request):
    auth = request.META.get('HTTP_AUTHORIZATION', b'')
    return auth


class TokenBackend:
    keyword = 'Token'
    model = None

    def get_model(self):
        if self.model is not None:
            return self.model
        return Token

    """
    A custom token model may be used, but must have the following properties.

    * key -- The string identifying the token
    * user -- The user to which the token belongs
    """

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower():
            return None

        if len(auth) == 1:
            msg = 'Invalid token header. No credentials provided.'
            raise AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = 'Invalid token header. Token string should not contain spaces.'
            raise AuthenticationFailed(msg)

        token = auth[1]

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise AuthenticationFailed('Invalid token.')

        if not token.user.is_active:
            raise AuthenticationFailed('User inactive or deleted.')
        return token.user