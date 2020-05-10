from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from blog.models import Profile,Projects
from webApi.serializers import QuizSerializer,QuestionSerializer,LanguageSerializer,ParadigmSerializer,ProgrammerSerializer
from webApi.models import *
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from webApi import utils

from rest_framework import authentication, permissions

def testAPI(request):
    # data = {'Name':'khan','phone':8010339935}
    data = Profile.objects.first()
    profile = ProfileSerializer(data, many = False)
    return JsonResponse(profile.data, status=201)

@api_view(['GET','POST'])
def testAPI2(request):
    # data = {'Name':'khan','phone':8010339935}
    data = Profile.objects.first()
    profile = ProfileSerializer(data, many = False)
    return Response(data = profile.data, status = status.HTTP_201_CREATED)

@api_view(['GET','POST'])
def getProjects(request):
    if request.method == 'GET':
        data = Projects.objects.all()
        projects = ProjectsSerializer(data, many = True)
        
        responseData = utils.displayData(projects.data,'success',status.HTTP_201_CREATED)
        return Response(responseData)
    if request.method == 'POST':
        print("===============")
        print(request.user)
        print(request.auth)
        data = {'data':{},'message':'This is a post method','status':201}
        responseData = utils.displayData(request.data,'post request',201)
        return Response(responseData)

#==================================Class Based Views====================================================
# ClassBAsed view has it own predefined method for particular request,so we do not have to check explicitly
class MessageView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    def get(self,request):
        responseData = utils.displayData(request.data,'This is a get Request',201)
        return Response(responseData)
    
    def post(self, request):
        responseData = utils.displayData(request.data,'This is a Post request ,based on class',201)
        return Response(responseData)



#==============================Class Based View======================================
# class QuizView(APIView):
#     def get_objects(self):
#         try:
#             return Quiz.objects.all()
#         except Quiz.DoesNotExist:
#             raise status.HTTP_404_NOT_FOUND
   
#     def get(self, request, format = None):
#         queryset = self.get_objects()
#         serializer = QuizSerializer(queryset, many = True)
#         return Response(data =  serializer.data, status = status.HTTP_200_OK)

#     def post(self, request):
#         serializer1 = QuizSerializer(data = request.data)
#         try:
#             if serializer1.is_valid():
#                 serializer1.save()
#                 return Response(data = serializer1.data, status = status.HTTP_201_CREATED)
#         except Exception as e:
#                 print(e)
#                 return Response(serializer1.errors, status = status.HTTP_404_NOT_FOUND)

#     def delete(self, request):
#         querySet = Quiz.objects.get(id = request.data['id'])
#         querySet.delete()
#         print(querySet)
#         return Response("deleted", status = status.HTTP_200_OK)

#     def put(self, request):
#         querySet = Quiz.objects.get(id = request.data['id'])
#         serializer1 = QuizSerializer(querySet, data = request.data)
#         if serializer1.is_valid():
#             serializer1.save()
#             return Response(data =serializer1.data,status = status.HTTP_202_ACCEPTED )
        
#         return Response(serializer1.errors,status = status.HTTP_404_NOT_FOUND )



#=============================generic Viw=================================
#generics.ListAPIView),generics.ListCreateAPIView
# class QuizView(generics.ListAPIView, generics.CreateAPIView):
#     queryset = Quiz.objects.all()
#     serializer_class = QuizSerializer


# =====================view Sets like a resource in other framework================
class QuizView(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

#========================Languages====================
class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer

class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer