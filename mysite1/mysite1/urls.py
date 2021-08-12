"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view),
    # http://127.0.0.1:8000/page/2003
    path('page/2003/', views.page_2003_view),
    path('page/2004/', views.page_2004_view),
    # 定义同一类型
    path('page/<int:page>/', views.int_view),
    # http://127.0.0.1:8000/20/add/20
    re_path(r'^(?P<x>\d{1,2})/(?P<op>\w+)/(?P<y>\d{1,2})$', views.cal2_view),
    path('<int:a>/<str:x>/<int:b>', views.cal_view),
    # http://127.0.0.1:8000/birthday/年4/月2/日2
    re_path(r'^birthday/(?P<y>\d{4})/(?P<m>\d{1,2})/(?P<d>\d{1,2})$', views.birthday_view),
    # http://127.0.0.1:8000/birthday/月2/日2/年4
    re_path(r'^birthday/(?P<m>\d{1,2})/(?P<d>\d{1,2})/(?P<y>\d{4})$', views.birthday_view),

    #  day 02
    path('test_request', views.test_request),
]
