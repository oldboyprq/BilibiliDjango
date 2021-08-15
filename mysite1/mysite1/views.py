from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

POST_FORM = '''
<form method = "post" action='/test_get_post'>
    用户名：<input type='text' name='uname'/>
    <input type='submit' value='提交'/>
</form>
'''


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
    # return HttpResponse('test request ok')
    return HttpResponseRedirect('/page/1')  # 重定向 路径以 '/' 开头


def test_get_post(request):
    if request.method == 'GET':
        print(request.GET)
        print(request.GET['a'])
        # 问卷调查  -from get 兴趣爱好  复选框
        print(request.GET.getlist('a'))
        print(request.GET.get('c', 'no c'))
        return HttpResponse(POST_FORM)
    elif request.method == "POST":
        # 处理用户提交数据
        print('uname is', request.POST['uname'])
        return HttpResponse('post is ok')
    else:
        pass

    return HttpResponse('--test_get_post is ok--')


def test_html(request):
    # 方案1
    # from django.template import loader
    # t = loader.get_template('test_html.html')
    # html = t.render()

    # 方案2
    from django.shortcuts import render
    dic = {'username': 'xiaomao', 'age': 18, }
    return render(request, 'test_html.html', dic)


def test_html_param(request):
    from django.shortcuts import render
    dic = dict()
    dic['int'] = 88
    dic['str'] = 'xiaomao'
    dic['lst'] = ['tony', 'jack', 'lily']
    dic['dict'] = {'a': 9, 'b': 10}
    dic['func'] = say_hi
    dic['class_obj'] = dog()
    dic['script'] = '<script>alert(1111)</script>'

    return render(request, 'test_html_param.html', dic)


def say_hi():
    return 'hahaha'


class dog:
    def say(self):
        return 'wangwang'


def test_if_for(request):
    dic = dict()
    dic['x'] = 10
    dic['lst'] = ['tom', 'jack', 'lily']
    return render(request, 'test_if_for.html', dic)


def test_mycal(request):
    if request.method == 'GET':
        return render(request, 'mycal.html')
    elif request.method == "POST":
        x = int(request.POST['x'])
        y = int(request.POST['y'])
        op = request.POST['op']
        if op == 'add':
            result = x + y
        elif op == 'sub':
            result = x - y
        elif op == 'mul':
            result = x * y
        elif op == 'div':
            result = x / y

        # locals()可以自动封装一个字典，省事
        return render(request, 'mycal.html', locals())


def base_view(request):
    lst = ['tony', 'jack']
    return render(request, 'base.html', locals())


def music_view(request):
    return render(request, 'music.html')


def sport_view(request):
    return render(request, 'sport.html')


def test_url(request):
    return render(request, 'test_url.html')


def test_url_result(request,age):
    # 302跳转
    from django.urls import reverse
    url = reverse('base_index')
    return HttpResponseRedirect(url)
    # return HttpResponse('--test url res is ok')
