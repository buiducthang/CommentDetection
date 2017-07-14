from django.conf.urls import url 
 
from . import views 
 
urlpatterns = [
    url(r'^$', views.Comment, name='comment'),
    url(r'^post/', views.Post, name='post'),
    url(r'^train/', views.AddTrain, name='addtrain'),
]