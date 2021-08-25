from django.shortcuts import render
from django.http import *


def test_static(request):
    return render(request, 'test_static.html')


def set_cookies(request):
    resp = HttpResponse('set cookie is ok')
    resp.set_cookie('uuname', 'gxn', 500)
    return resp


def get_cookies(request):
    value = request.COOKIES.get('uuname')
    return HttpResponse('value is %s' % value)


def set_session(request):
    request.session['uuname'] = 'wwc'
    return HttpResponse('set session is ok')


def get_session(request):
    value = request.session['uuname']
    return HttpResponse('value is %s' % value)
