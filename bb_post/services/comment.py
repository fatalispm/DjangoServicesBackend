from django.db import IntegrityError

from bb_post.models import Comment
from utils.api.exceptions import RequestValidationFailedAPIError


def create(text, user, post):
    try:
        return Comment.objects.create(text=text, user=user, post_id=post)
    except IntegrityError:
        raise RequestValidationFailedAPIError('Post does not exist')