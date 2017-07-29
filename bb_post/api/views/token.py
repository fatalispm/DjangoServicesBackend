from django.views.generic import View

from bb_post.api.forms.user import CreateForm
from bb_post.api.serializers.token import serialize_token
from utils.api.exceptions import RequestValidationFailedAPIError
from utils.api.mixins import APIMixin

import bb_post.services.token


class GetTokenView(APIMixin, View):

    def post(self, request, parameters, *args, **kwargs):

        form = CreateForm(data=parameters)

        if not form.is_valid():
            raise RequestValidationFailedAPIError(form.errors)
        token = bb_post.services.token.get_token(**form.cleaned_data)
        return serialize_token(token)