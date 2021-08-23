from django.shortcuts import render
from .models import Book
from django.http import *


# Create your views here.
def all_book(request):
    all_book = Book.objects.filter(is_active=True)
    return render(request, 'bookstore/all_book.html', locals())


def update_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id, is_active=True)
    except Exception as e:
        print('--update book error is %s' % e)

    if request.method == 'GET':
        return render(request, 'bookstore/update_book.html', locals())
    elif request.method == 'POST':
        price = request.POST['price']
        market_price = request.POST['market_price']

        book.price = price
        book.market_price = market_price
        book.save()
        return HttpResponseRedirect('/bookstore/all_book')


def delete_book(request):
    # 通过获取查询字符串获取book_id
    book_id = request.GET.get('book_id')
    if not book_id:
        return HttpResponse('----请求异常')
    try:
        book = Book.objects.get(id=book_id, is_active=True)
    except Exception as e:
        print('----delete book get error %s' % e)
        return HttpResponse('-----The book id is error')
    # is_active改成False
    book.is_active = False
    book.save()
    # 302跳转到all_book
    return HttpResponseRedirect('/bookstore/all_book')
