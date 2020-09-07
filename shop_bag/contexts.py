from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_products(request):

    bag_items = []
    total_items = 0
    product_count = 0
    shop_bag = request.session.get('shop_bag', {})

    for product_id, item_data in shop_bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=product_id)
            total_items += item_data * product.price
            product_count += item_data
            bag_items.append({
                'product_id': product_id,
                'product_quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=product_  id)
            for size, product_size in item_data['items_by_size'].items():
                total_items += product_quantity * product.price
                product_count += product_quantity
                bag_items.append({
                    'product_id': product_id,
                    'product_quantity': item_data,
                    'product': product,
                    'size': size,
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