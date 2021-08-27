from django.shortcuts import render
from django.http import *
from .models import User
import hashlib


# Create your views here.
def reg_view(request):
    # 注册
    # get 返回页面
    if request.method == "GET":
        return render(request, 'user/register.html')

    elif request.method == "POST":
        # post 处理提交数据
        # 两个密码一致，当前用户名是否可用 插入数据
        username = request.POST['username']
        password1 = request.POST['password_1']
        password2 = request.POST['password_2']
        if password1 != password2:
            return HttpResponse('两次密码输入不一致')
        # 哈希算法 给定明文，计算出一段定长的不可逆的值；md5 sha-256
        # 特点
        # 定长输入，输出长度与输入无关 md5(32位 16进制）
        # 不可逆 无法反向计算出对应的明文
        # 雪崩效应 输入改变，输出必然变化
        # 场景：1、密码处理  2、文件完整性校验
        # 如何使用
        m = hashlib.md5()
        m.update(password1.encode())  # 注意参数是字节串
        password_md5 = m.hexdigest()
        old_user = User.objects.filter(name=username)
        if old_user:
            return HttpResponse('用户名已注册')
        # create有报错风险 同时注册并发写入 同时执行到create只有一个成功，其余报错
        try:
            user = User.objects.create(name=username, password=password_md5)
        except Exception as e:
            print('--create use error %s' % e)
            return HttpResponse('用户名已注册')
        request.session['username'] = username
        request.session['uid'] = user.id
        # 修改session存储时间为1天
        request.session['session_cookie_age'] = 3600 * 24
        return HttpResponseRedirect('/index')


def login_view(request):
    if request.method == "GET":
        # 检查登录状态
        # 检查session
        if request.session.get('username') and request.session.get('uid'):
            return HttpResponseRedirect('/index')
        # 无数据检查cookie
        c_username = request.COOKIES.get('username')
        c_uid = request.COOKIES.get('uid')
        if c_username and c_uid:
            # 回写session
            request.session['username'] = c_username
            request.session['uid'] = c_uid
            # return HttpResponse('已登录')
            return HttpResponseRedirect('/index')
        else:
            # cookie无数据返回login
            return render(request, 'user/login.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # 校验用户是否存在
        try:
            user = User.objects.get(name=username)
        except Exception as e:
            print('--login user error %s' % e)
            return HttpResponse('用户名或密码错误')
        # 校验密码是否正确
        m = hashlib.md5()
        m.update(password.encode())
        if m.hexdigest() != user.password:
            return HttpResponse('用户名或密码错误')
        # 记录会话状态
        request.session['username'] = username
        request.session['uid'] = user.id
        # resp = HttpResponse('登录成功')
        resp = HttpResponseRedirect('/index')
        # 判断用户是否点选记住用户名
        if 'remember' in request.POST:
            resp.set_cookie('username', username, 3600 * 24 * 3)
            resp.set_cookie('uid', user.id, 3600 * 24 * 3)
        return resp


def logout_view(request):
    # 删除session
    if 'username' in request.session:
        del request.session['username']
    if 'uid' in request.session:
        del request.session['uid']
    # 删除cookie
    resp = HttpResponseRedirect('/index')
    if 'username' in request.COOKIES:
        resp.delete_cookie('username')
    if 'uid' in request.COOKIES:
        resp.delete_cookie('uid')
    return resp
