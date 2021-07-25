import json

from urllib import parse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . import run
from . import ini

# Create your views here.
@csrf_exempt
def Judge(request):
    if not ini.OpenJudge:
        return HttpResponse("404!")

    Data = json.loads(request.body)
    
    if Data["password"] != ini.JudgeServersPassword:
        return HttpResponse("404!")
    
    Result = run.PostCompile(ini.JudgesUrl, 
                             ini.XJudgeServerTokens,
                             parse.unquote(Data['Code']), 
                             Data['Time'], 
                             Data['Memory'], 
                             Data['Language'], 
                             ini.TestCaseRode, 
                             Data['Case'])

    return HttpResponse(json.dumps(Result))  
