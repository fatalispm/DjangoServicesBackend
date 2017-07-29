from django.utils.functional import SimpleLazyObject

from bb_post.common.backends import TokenBackend


class TokenAuthMiddleware(object):
    def process_request(self, request):
        request.user = SimpleLazyObject(lambda: TokenBackend().authenticate(
            request))
