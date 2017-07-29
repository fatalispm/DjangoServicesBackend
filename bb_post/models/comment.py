from django.conf import settings
from django.db import models

from bb_post.models import Post


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post, related_name='comments')

    class Meta:
        app_label = 'bb_post'
        db_table = 'bp_comment'
