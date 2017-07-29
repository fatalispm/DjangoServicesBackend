from utils.api.exceptions import APIError


class UserAPIError(APIError):
    pass


class UserBadCredentialsError(UserAPIError):
    code = 'user_wrong_credentials'


class AuthenticationFailed(UserAPIError):
    code = 'user_wrong_token'
