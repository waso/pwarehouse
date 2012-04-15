from django import template

register = template.Library()

@register.filter
def get_price_by_index(value, arg):
    try:
    	return '{0:.2f}'.format(value[arg])
    except Exception, e:
    	return ''