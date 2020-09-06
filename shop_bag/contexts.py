from decimal import Decimal
from django.conf import settings

def bag_products(request):

    bag_items = []
    total_items = 0
    product_count = 0

    if total_items < settings.FREE_DELIVERY:
        delivery_fee = total_items * Decimal(settings.DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY - total_items
    else:
        delivery_fee = 0
        free_delivery_delta = 0
    
    shop_total = delivery_fee + total_items
    
    context = {
        'bag_items': bag_items,
        'total_items': total_items,
        'product_count': product_count,
        'delivery_fee': delivery_fee,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery': settings.FREE_DELIVERY,
        'shop_total': shop_total,
    }

    return context