from django.contrib.comments.models import Comment
from django.contrib.comments.managers import CommentManager

class CommentManager(CommentManager):
    def get_query_set(self):
        return (super(CommentManager, self)
            .get_query_set()
            .select_related('user__profile'))

Comment.add_to_class('objects', CommentManager())
