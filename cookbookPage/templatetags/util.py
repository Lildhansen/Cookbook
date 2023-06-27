from django import template

register = template.Library()

@register.filter
def modulo(num, val):
    return num % val

@register.filter
def anyRecipeIsBeingEdited(recipes):
    for recipe in recipes:
        if recipe.isBeingEdited:
            return True
    return False
        