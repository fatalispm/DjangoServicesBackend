def serialize_comment(comment, many=False):
    if not many:
        return dict(
            text=comment.text,
            post=comment.post.id,
            user=comment.user.email
        )
    return [serialize_comment(c) for c in comment]
