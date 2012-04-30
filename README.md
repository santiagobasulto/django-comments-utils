django-comments-utils
=====================

A set of utilities to easy developing using the Django Comments Framework.

## Motivation

I've started coding a big app that makes heavy use of Django Comments. So i'll start to share all these utilities I create for my own use.

## Utilites

### Templatetags

####get_last_comments:

A simple templatetag that returns comments sorted by publish date, in descending order. This is the syntax, asuming a Post has comments:

    {% get_last_comments for post as last_comments %}
    
    {% for comment in last_comments %}
        {# Using comment #}
    {% endfor%}
    
It receives an optional limit parameter:

    {% get_last_comments for post as last_comments %}
    
    {% for comment in last_comments limit 2 %}
        {# Using comment #}
    {% endfor%}

This behavior is inspired in Facebook, that grabs last 2 comments from a big conversation in order to make this better for the user.

### Managers

There's one manager in manager.py that makes `select_related()` of models `User` and `Profile`. It's a big preformance improvement. I recommend you to use it anytime you can.

