from django.shortcuts import render

# Create your views here.


def profile(request):
    """ Display the user's profile. """

    template = 'user_profile/user-profile.html'
    context = {}

    return render(request, template, context)