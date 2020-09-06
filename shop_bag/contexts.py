from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_products(request):

    bag_items = []
    total_items = 0
    product_count = 0
    shop_bag = request.session.get('shop_bag', {})

    for product_id, product_quantity in shop_bag.items():
        product = get_object_or_404(Product, pk=product_id)
        total_items += product_quantity * product.price
        product_count += product_quantity
        bag_items.append({
            'product_id': product_id,
            'product_quantity': product_quantity,
            'product': product,
        })

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