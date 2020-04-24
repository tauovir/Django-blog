
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from ..models import Profile,Employment,Projects,Technologies
from django.conf import settings
import json
from ..errorMessage import getApiMsg
import re 
# Create your views here.


def portfolio_view(request):
    # querySet = Employment.objects.all()
    # profileData = querySet[0]
    # context = {'data':querySet,'profileData' : profileData}
    # print(profileData.profile.last_name)
    # #print(data['data'][0].profile.first_name)
    #for e in data
    querySet = Projects.objects.all()
    formatedData = makeData(querySet)
    print(formatedData)
    context = {'formatedData' :formatedData }
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
