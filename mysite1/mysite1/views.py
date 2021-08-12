from django.http import HttpResponse


def page_2003_view(request):
    html = "<h1>这是第一个页面</h1>"
    return HttpResponse(html)


def page_2004_view(request):
    html = "<h1>这是第二个页面</h1>"
    return HttpResponse(html)


def index_view(request):
    html = "<h1>这是主页</h1>"
    return HttpResponse(html)


def int_view(request, page):
    html = "<h1>这是数字{}</h1>".format(page)
    return HttpResponse(html)


def cal_view(request, a, x, b):
    if x not in ['add', 'sub', 'mul']:
        return HttpResponse('Your x is wrong')

    result = 0
    if x == 'add':
        result = a + b
    elif x == 'sub':
        result = a - b
    elif x == 'mul':
        result = a * b

    return HttpResponse("结果为:%s" % result)


def cal2_view(request, x, op, y):
    html = "x:%s op:%s y:%s" % (x, op, y)
    return HttpResponse(html)


def birthday_view(request, y, m, d):
    html = "生日为%s年%s月%s日" % (y, m, d)
    return HttpResponse(html)


def test_request(request):
    print('path info is', request.path_info)
    print('method is ', request.method)
    print('querystring is ', request.GET)
    print('full path is', request.get_full_path())
    return HttpResponse('test request ok')
