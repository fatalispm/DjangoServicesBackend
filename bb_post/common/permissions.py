from django.contrib.auth.models import AnonymousUser


def is_authenticated(request):
    return not isinstance(request.user, AnonymousUser)