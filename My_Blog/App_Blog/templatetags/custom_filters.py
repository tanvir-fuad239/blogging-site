from django import template


register = template.Library()

def range_of_words(value):

    return value[0:300] + "....."

register.filter('range_of_words', range_of_words)