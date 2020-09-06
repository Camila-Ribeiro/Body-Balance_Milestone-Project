from django.shortcuts import render

# Create your views here.


def shop_bag(request):
    """ A view that renders the shopping bag page """

    return render(request, 'shop_bag/shop-bag.html')