from django.contrib import admin
from .models import Book
from .models import Author


# Register your models here.
class BookManager(admin.ModelAdmin):
    # 列表页显示哪些字段的列
    list_display = ['id', 'title', 'pub', 'price']
    # 控制list_display中哪些可以链接到修改页面
    list_display_links = ['title']
    # 添加过滤器
    list_filter = ['pub']
    # 添加搜索框,根据输入字段进行模糊查询
    search_fields = ['title', 'id']
    # 添加所在列表页编辑的字段，注意与link_display_links互斥
    list_editable = ['price']


class AuthorManager(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'email']


admin.site.register(Book, BookManager)
admin.site.register(Author, AuthorManager)
