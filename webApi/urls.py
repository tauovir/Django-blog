from django.urls import include, path
from rest_framework import routers
from . import views

print("================I am Here ========================")
router = routers.DefaultRouter()
router.register('v1/quiz', views.QuizView)
router.register('languages', views.LanguageView)
router.register('paradigms', views.ParadigmView)
router.register('programmers', views.ProgrammerView)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('v1/test', views.testAPI,name='testApi'),
    path('v1/test2', views.testAPI2,name='testApi2'),
    path('v1/projects', views.getProjects,name='getProject'),
    path('v1/message/', views.MessageView.as_view(),name='message'),
     #path('v1/quiz/', views.QuizView.as_view(),name='message'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
urlpatterns += router.urls