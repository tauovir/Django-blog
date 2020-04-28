from django.urls import path
from blog import views
#import .views
#from blog.views import portfolio


urlpatterns = [
    path('', views.post, name='post'),
    path('page<int:num>/', views.post,name='post'),
    path('about/', views.about, name='about'),
    path('post_detail/<slug:slug>', views.post_detail_view, name='post_detail'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('comment-redirect', views.commentRedirect, name='commentRedirect'),
    path('comments', views.saveComment, name='saveComment'),
    path('contactus/', views.saveContact, name='saveContact'),
    
]