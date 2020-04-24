"""
Purpose: This is custome template filter which can be used in template

"""
from django import template

# we need to make sure that your templates are added to the existing library of tags and filters that Django knows about.
# This statement gives an instance of the library so you can register your filters as you go about creating them
register = template.Library()
# create decorator and difine our filter name
@register.filter(name='splitString')

def splitString(str1,sep):
    return str1.split(sep)