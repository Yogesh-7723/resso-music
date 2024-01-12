from django.urls import path
from . import  views
from django.conf import settings 
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index),
    path('createsong/',views.createsong),
    path('newsong/',views.newsong),
    path('updateview/',views.updateview),
    path('update/<int:qk>/',views.update),
    path('delete/<int:uid>/',views.delete,name='delete'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
