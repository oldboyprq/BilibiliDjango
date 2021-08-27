from django.urls import path
from . import views

urlpatterns = [
    path('all', views.list_view),
    path('add', views.add_note),
    path('update_note/<int:note_id>', views.update_view),
    path('delete_note',views.delete_view)
]