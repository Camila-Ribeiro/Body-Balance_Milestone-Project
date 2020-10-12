from django import template

register = template.Library()


@register.filter(name='calc_productXquantity')
def calc_productXquantity(price, product_quantity):
    return price * product_quantity
