from django import template

register = template.Library()


@register.filter
def format_name(firstname, lastname):
    if len(lastname) > 7:
        return f"{firstname} {lastname[0]}."
    if len(firstname) > 10 and len(firstname) > 10:
        return f"{firstname[0]} {lastname[0]}."

    return f"{firstname} {lastname}"
