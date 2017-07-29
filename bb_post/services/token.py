from bb_post.models.token import Token


def get_token(user, **kwargs):
    token, created = Token.objects.get_or_create(user=user)
    return token