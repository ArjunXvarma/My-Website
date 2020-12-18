from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, PortfolioPost

# Create your views here.
def index(request):
    context = {
        'posts': PortfolioPost.objects.all()
    }
    return render(request, 'Site/index.html', context)
