from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_products(request):

    bag_items = []
    total_items = 0
    product_count = 0
    shop_bag = request.session.get('shop_bag', {})
    get_cat = None
    get_plan_total = None

    for product_id, item_data in shop_bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=product_id)
            category = product.category

            #  get nutrition plan category
            get_cat = category.category_name
            total_items += item_data * product.price
            product_count += item_data

            # get_plan_total = product.price

            if get_cat == 'nutrition_plan':
                nut_price = round(product.price * Decimal
                                  (settings.DELIVERY_PERCENTAGE / 100), 2)
                get_plan_total = product.price
                product_in_bag = product.product_name
            bag_items.append({
                'product_id': product_id,
                'product_quantity': item_data,
                'product': product,
                'category': category,
            })

        else:
            product = get_object_or_404(Product, pk=product_id)
            for size, product_quantity in item_data['items_by_size'].items():
                total_items += product_quantity * product.price
                product_count += product_quantity
                bag_items.append({
                    'product_id': product_id,
                    'product_quantity': product_quantity,
                    'product': product,
                    'size': size,
                })

    #  no delivery fee if nutrition plan in shop bag
    if total_items < settings.FREE_DELIVERY:
        if total_items == get_plan_total and get_cat == 'nutrition_plan':
            delivery_fee = 0
            free_delivery_delta = 0
        elif get_cat == 'nutrition_plan' and product_in_bag:
            delivery_fee = (total_items - get_plan_total) * Decimal(settings.DELIVERY_PERCENTAGE / 100)
            free_delivery_delta = 0
        else:
            if get_plan_total:
                delivery_fee = (total_items - get_plan_total)\
                              * Decimal(settings.DELIVERY_PERCENTAGE / 100)
                free_delivery_delta = settings.FREE_DELIVERY - total_items
            else:
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
