from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,re_path
from . import views


urlpatterns = [

    path('',views.read_item,name='item_list'),
    path('create/',views.create_item,name='create_item'),
    path('update/<int:pk>',views.update_item,name='update_item'),
    path('delete/<int:pk>',views.delete_item,name='delete_item'),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
  