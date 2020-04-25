
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from ..models import Profile,Employment,Projects,Technology_Category
from django.conf import settings
import json
from ..errorMessage import getApiMsg
import re 
# Create your views here.


def portfolio_view(request):
    querySet = Projects.objects.all()
    formatedData = makeData(querySet)
    catTechSet = Technology_Category.objects.all()
    techList, otherTech  = formatTechnology(catTechSet)

    educationSet = Profile.objects.first().educations_set.filter(is_school = 0)
    educationData = [{'short_name' : x.course_short_name,'full_name' :x.course_full_name,'start_year':x.start_year,'end_year':x.end_year} for x in educationSet]
    certificateSet = Profile.objects.first().certificates_set.all()
    certificateData = [{'name' : x.name,'short_name':x.short_name,'institute_short_name' : x.institute_short_name} for x in certificateSet]
    interestSet = Profile.objects.first().user_interest_set.all()
    intresteList = [ x.name for x in interestSet]

    context = {
        'formatedData' :formatedData,
        'techData':techList,
        'otherTech' : otherTech,
        'educationData' : educationData,
        'certificateData' : certificateData,
        'intresteList' : intresteList,
        
        }
    return render(request, 'portfolio.html', context)
   

"""
formate data for templae so that we can easily retrieve it
"""
def makeData(querySet):
    # Initialize dictionar and list
    employmentList = []
    projectList = []
    resultData = {}
    employmentData = {}

    for projects in querySet:
        # Employment Dictionary
        if not any(d['id'] == projects.employment.id for d in employmentList): # Check id in list of dictionary
            projectList = []
            projectData = {}
            # bind projects data
            projectData['id'] = projects.id
            projectData['name'] = projects.name
            projectData['team_size'] = projects.team_size
            projectData['description'] = projects.description
            projectData['role_responsibility'] = projects.role_responsibility
            tempTechList = projects.technology.all().values('name')
            techList = [x['name'] for x in tempTechList]
            projectData['technology'] = techList
            projectList.append(projectData)
            # Bind Employement data
            employmentData = {
            'id' : projects.employment.id,
            'employer': projects.employment.employer,
            'position': projects.employment.position,
            'summary': projects.employment.summary,
            'start_date': projects.employment.start_date,
            'end_date': projects.employment.end_date,
            'is_current_org': projects.employment.is_current_org,
            'projects': projectList,
                }
            employmentList.append(employmentData)
        else:
            ## Bind project data with its associate company.employement
            projectData = {}
            projectData['id'] = projects.id
            projectData['name'] = projects.name
            projectData['team_size'] = projects.team_size
            projectData['description'] = projects.description
            projectData['role_responsibility'] = projects.role_responsibility
            tempTechList = projects.technology.all().values('name')
            techList = [x['name'] for x in tempTechList]
            projectData['technology'] = techList
            projectList.append(projectData)
            
            for emp in employmentList:
                if emp['id'] == projects.employment.id:
                   emp['projects'] = projectList # Append new project at appropreate index
                   break
        resultData = {
                'id' : projects.employment.profile.id,
                'name' : projects.employment.profile.middle_name +" " + projects.employment.profile.last_name,
                'profile_title' : projects.employment.profile.profile_title,
                'email' : projects.employment.profile.email,
                'mobile_number' : projects.employment.profile.mobile_number,
                'brief_summary' : projects.employment.profile.brief_summary,
                'employments' : employmentList,
            
        }

        
    return resultData


# Formatting Technology data
def formatTechnology(catTechSet):
    catList = []
    otherTech = []
    for cat in catTechSet:
        if cat.name == 'Others':
            tempOther = cat.technologies_set.all()
            otherTech = [x.name for x in tempOther]
        else:
            techList = []
            catTemp = {'name' : cat.name}
            temp = cat.technologies_set.all()
            techList = [{'name' : x.name,'version':x.version,'rate':x.rate} for x in temp]
            catTemp = {cat.name : techList}
            catList.append(catTemp)

    return catList,otherTech



"""
cat = Technology_Category.objects.get(pk = 1)
cat.technologies_set.all()
cat1 = Technology_Category.objects.all();
for ct in cat1:
    ...:     print(ct.technologies_set.all())

"""