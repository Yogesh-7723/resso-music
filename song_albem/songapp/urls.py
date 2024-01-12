from django.urls import path
from . import  views
from django.conf import settings 
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index),
    path('createsong/',views.createsong),
    path('newsong/',views.newsong),
    path('update/<int:uid>/',views.update),
    path('updateview/<int:uid>/',views.updateview,name='updateview'),
    path('delete/<int:qk>/',views.delete,name='delete'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
