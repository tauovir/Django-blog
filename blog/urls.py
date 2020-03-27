from django.urls import path
from blog import views


urlpatterns = [
    path('', views.post, name='post'),
    path('page<int:num>/', views.post,name='post'),
    path('about/', views.about, name='about'),
    path('post_detail/<slug:slug>', views.post_detail_view, name='post_detail'),
    path('subscribe/', views.subscribe, name='subscribe'),
    
]