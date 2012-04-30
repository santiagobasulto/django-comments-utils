from django import template
from django.contrib.comments.models import Comment

register = template.Library()

def do_get_last_comments(parser, token):
    """
    Get last comments for a given object
    a limit can be specified.

    Example usage:
        {% get_last_comments for [object] as [varname] %}
        {% get_last_comments for [object] as [varname] limit [ammount] %}
    """

    keywords = token.contents.split()
    if len(keywords) != 5 and len(keywords) != 7:
        raise template.TemplateSyntaxError("'%s' tag takes exactly 2 or 4 arguments" % keywords[0])
    if keywords[1] != 'for':
        raise template.TemplateSyntaxError("first argument to '%s' tag must be 'for'" % keywords[0])
    if keywords[3] != 'as':
        raise template.TemplateSyntaxError("first argument to '%s' tag must be 'as'" % keywords[0])
    if len(keywords) > 5 and keywords[5] != 'limit':
        raise template.TemplateSyntaxError("third argument to '%s' tag must be 'limit'" % keywords[0])
    if len(keywords) > 5:
        return GetLastCommentsNode(keywords[2], keywords[4],keywords[6])
    return GetLastCommentsNode(keywords[2],keywords[4])

class GetLastCommentsNode(template.Node):

    def __init__(self, obj, varname, limit=2):
        self.obj = obj
        self.varname = varname
        self.limit = int(limit)

    def render(self, context):
        obj = None
        try:
            obj = template.resolve_variable(self.obj, context)
        except template.VariableDoesNotExist:
            return ''
        try:
            qs = Comment.objects.for_model(obj.__class__).filter(object_pk=obj.pk)
            qs = qs.order_by("-submit_date")[:self.limit]
            context[self.varname] = qs
            return ''
        except:
            context[self.context_var] = ''
            return ''

register.tag('get_last_comments', do_get_last_comments)
