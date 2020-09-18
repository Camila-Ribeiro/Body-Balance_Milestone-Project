from django.shortcuts import render

# Create your views here.


def shop_nutrition_plan(request):
    """ A view to return the index page """

    return render(request, 'nutrition/nutrition.html')

