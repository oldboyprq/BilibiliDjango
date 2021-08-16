from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/music/index
    path('index', views.index_view),  # 匹配子路由 从music后开始匹配

]
