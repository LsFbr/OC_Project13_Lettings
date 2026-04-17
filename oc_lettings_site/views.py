from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

# For testing 500 errors
def trigger_500_error(request):
    return 1 / 0
