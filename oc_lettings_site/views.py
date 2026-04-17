from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def trigger_500_error(request):
    return 1 / 0
