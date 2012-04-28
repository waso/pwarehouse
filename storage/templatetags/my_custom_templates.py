from django import template

register = template.Library()

@register.filter
def get_price_by_index(value, arg):
    try:
    	return '{0:.2f}'.format(value[arg])
    except Exception, e:
    	return ''

@register.filter
def format_price(value):
    try:
    	return '{0:.2f}'.format(float(value))
    except Exception, e:
    	return 'ERROR'

@register.filter
def get_value_by_key(value, key):
	for item in value:
		if key == item[0]:
			return item[1]
	return ''

@register.filter
def is_false(arg): 
    return arg is False

@register.filter
def is_true(arg): 
    return arg is True