from django.contrib import admin

from bb_post.models import Post
from bb_post.models.token import Token

admin.site.register(Post)
admin.site.register(Token)