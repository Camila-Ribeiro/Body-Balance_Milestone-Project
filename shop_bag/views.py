from django.shortcuts import render, redirect

# Create your views here.


def shop_bag(request):
    """ A view that renders the shopping bag page """

    return render(request, 'shop_bag/shop-bag.html')


def add_products_to_bag(request, product_id):
    """ Add a quantity of the specified product to the shopping bag """

    product_quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shop_bag = request.session.get('shop_bag', {})

    if product_id in list(shop_bag.keys()):
        shop_bag[product_id] += product_quantity
    else:
        shop_bag[product_id] = product_quantity

    request.session['shop_bag'] = shop_bag
    return redirect(redirect_url)