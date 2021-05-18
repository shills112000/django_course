from django import template
register = template.Library()

def cut(value,arg):
    """
    This cuts all value of arg from string
    """
    return value.replace(arg,"")

register.filter('cut',cut)  #First paramter 'cut' is the string , second paramter is the function cut