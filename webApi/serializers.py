from rest_framework import serializers

from rest_framework.serializers import ModelSerializer
from webApi.models import Quiz,Question,Language,Paradigm,Programmer
# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ['first_name','middle_name','last_name','profile_title','brief_summary','email','mobile_number']

# class ProjectsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Projects
#         fields = ['name','employment','description','team_size','start_date','end_date','technology']

class QuizSerializer(ModelSerializer):
    class Meta:
        model = Quiz
        # fields = ['name','description']
        fields = '__all__'

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta :
        model = Language
        fields = ['id','url','name','paradigm']


class ParadigmSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta :
        model = Paradigm
        fields = ['id','url','name']

class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta :
        model = Programmer
        fields = ['id','url','name','languages'] 