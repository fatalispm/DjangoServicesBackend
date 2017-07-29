from django.views.generic import View

from bb_post.api.forms.comment import CreateForm
from bb_post.api.serializers.comment import serialize_comment
from bb_post.common.permissions import is_authenticated
from utils.api.exceptions import RequestValidationFailedAPIError
from utils.api.mixins import APIMixin

import bb_post.services.comment


class Collection(APIMixin, View):
    permission_classes = (is_authenticated,)

    def post(self, request, parameters, *args, **kwargs):
        form = CreateForm(data=parameters)
        if not form.is_valid():
            raise RequestValidationFailedAPIError(form.errors)
        form.cleaned_data['user'] = request.user

        comment = bb_post.services.comment.create(**form.cleaned_data)

        return serialize_comment(comment)
