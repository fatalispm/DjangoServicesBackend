from . import comment


def serialize(post):
    serialized_post = serialize_id(post)
    serialized_comments = comment.serialize_comment(post.comments.all(),
                                                    many=True)
    serialized_post.update({
        'subject': post.subject,
        'content': post.content,
        'comments': serialized_comments
    })

    return serialized_post


def serialize_id(post):
    return {
        'id': post.id
    }
