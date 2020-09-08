from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.


def shop_bag(request):
    """ A view that renders the shopping bag page """

    return render(request, 'shop_bag/shop-bag.html')


def add_products_to_bag(request, product_id):
    """ Add a quantity of the specified product to the shopping bag """

    product_quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_item_size' in request.POST:
        size = request.POST['product_item_size']
    shop_bag = request.session.get('shop_bag', {})
   
    if size:
        if product_id in list(shop_bag.keys()):
            if size in shop_bag[product_id]['items_by_size'].keys():
                shop_bag[product_id]['items_by_size'][size] += product_quantity
            else:
                shop_bag[product_id]['items_by_size'][size] = product_quantity
        else:
            shop_bag[product_id] = {'items_by_size': {size: product_quantity}}
    else:
        if product_id in list(shop_bag.keys()):
            shop_bag[product_id] += product_quantity
        else:
            shop_bag[product_id] = product_quantity

    request.session['shop_bag'] = shop_bag
    return redirect(redirect_url)


def update_quantity_bag(request, product_id):
    """Update the quantity of the specified product to the specified amount"""

    product_quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_item_size' in request.POST:
        size = request.POST['product_item_size']
    shop_bag = request.session.get('shop_bag', {})

    if size:
        if product_quantity > 0:
            shop_bag[product_id]['items_by_size'][size] = product_quantity
        else:
            del shop_bag[product_id]['items_by_size'][size]
            if not shop_bag[product_id]['items_by_size']:
                shop_bag.pop(product_id)
    else:
        if product_quantity > 0:
            shop_bag[product_id] = product_quantity
        else:
            shop_bag.pop(product_id)

    request.session['shop_bag'] = shop_bag
    return redirect(reverse('shop_bag'))


def remove_product_from_bag(request, product_id):
    """Remove the product from the shopping bag"""

    try:
        size = None
        if 'product_item_size' in request.POST:
            size = request.POST['product_item_size']
        shop_bag = request.session.get('shop_bag', {})

        if size:
            del shop_bag[product_id]['items_by_size'][size]
            if not shop_bag[product_id]['items_by_size']:
                shop_bag.pop(product_id)

        else:
            shop_bag.pop(product_id)

        request.session['shop_bag'] = shop_bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
