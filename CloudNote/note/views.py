from django.shortcuts import render
from django.http import *
from .models import Note


def check_login(fn):
    def wrap(request, *args, **kwargs):
        if 'username' not in request.session or 'uid' not in request.session:
            c_username = request.COOKIES.get('username')
            c_uid = request.COOKIES.get('uid')
            if not c_uid or not c_username:
                return HttpResponseRedirect('/user/login')
            else:
                request.session['username'] = c_username
                request.session['uid'] = c_uid
        return fn(request, *args, **kwargs)

    return wrap


# Create your views here.
@check_login
def add_note(request):
    if request.method == "GET":
        return render(request, 'note/add_note.html')
    elif request.method == "POST":
        uid = request.session['uid']
        title = request.POST['title']
        content = request.POST['content']

        Note.objects.create(title=title, content=content, user_id=uid)
        return HttpResponseRedirect('/note/all')


@check_login
def list_view(request):
    uid = request.session['uid']
    username = request.session['username']
    notes = Note.objects.filter(user_id=uid)
    return render(request, 'note/list_note.html', locals())


@check_login
def update_view(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Exception as e:
        return HttpResponse('the error is %s' % e)
    if request.method == "GET":
        return render(request, 'note/update_note.html', locals())
    elif request.method == "POST":
        note.title = request.POST['title']
        note.content = request.POST['content']
        note.save()
        return HttpResponseRedirect('/note/all')


@check_login
def delete_view(request):
    note_id = request.GET.get('note_id')
    try:
        Note.objects.filter(id=note_id).delete()
    except Exception as e:
        return HttpResponse('the error is %s' % e)
    return HttpResponseRedirect('/note/all')
