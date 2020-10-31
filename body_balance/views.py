from django.shortcuts import render


def handler404(request, exception):
    '''
    A 404 error handling view
    '''
    return render(request, '404.html')


def handler500(request, exception):
    '''
    A 500 error handling view
    '''
    return render(request, '500.html')
