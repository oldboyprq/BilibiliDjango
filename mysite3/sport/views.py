from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# Create your views here.
def index_view(request):
    return HttpResponse('这是体育频道首页')