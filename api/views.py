import json
import requests
import time
import queue

from django.shortcuts import render
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

from . import models
from . import ini


ServersQueue = queue.Queue()

for i in range(0, ini.ServersNum):
    ServersQueue.put(i)


# Create your views here.
def Run(request):
    if request.method != 'POST':
        return HttpResponse("Method isn't allowed! ")
    
    if not ini.OpenApi:
        return HttpResponse("404!")
    
    Req = json.loads(request.body)
    Req["password"] = ini.ServersPassword
    
    Data = {"headers" : {"Content-type" : "application/json"}}
    Data["json"] = Req
    
    while ServersQueue.empty():
        time.sleep(0.05)
    
    NowServer = ServersQueue.get()
    
    Result = requests.post(ini.ServersUrls[NowServer], **Data)
    
    ServersQueue.put(NowServer)
    
    Res = json.loads(Result.text)
    Res["Name"] = ini.Names[NowServer]
    Res["type"] = 1
    
    return HttpResponse(json.dumps(Res))
    
@csrf_exempt
def Login(request):
    
    print("rece!")
    
    if request.method != 'POST':
        return HttpResponse("Method isn't allowed! ")
    
    if not ini.OpenApi:
        return HttpResponse("404!")
        
    Req = json.loads(request.body)
    
    try:
        IsLogin = models.Users.objects.get(name = Req["Name"], password = Req["Password"]).name
    except models.Users.DoesNotExist:
        IsLogin = "-1"
    
    return HttpResponse(IsLogin)
    
    
def register(request):
    
    if request.method != 'POST':
        return HttpResponse("Method isn't allowed! ")
    
    if not ini.OpenApi:
        return HttpResponse("404!")
        
    print(request.body)
    
    Req = json.loads(request.body)
    
    NewUser = models.Users()
    
    NewUser.name = Req["Name"]
    NewUser.email = Req["Email"]
    NewUser.password = Req["Password"]
    NewUser.number = 20
    
    NewUser.save()
    
    return HttpResponse("0")
    
    
    
    
    