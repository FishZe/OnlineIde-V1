from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.context_processors import csrf

from . import ini


# Create your views here.

def Index(request):
    if not ini.OpenWeb:
        return HttpResponse("404!")
       
    request.encoding = 'utf-8'
    if 'language' in request.GET and request.GET['language']:
        Lang = request.GET['language']
        print(Lang)
    else:
        Lang = "cpp"
    
    Select = SelectDict = {"cpp" : "", "c" : "", "python2" : "", "python3" : "", "java" : "", "go" : ""}
    Select[Lang] = "Selected"
    
    return render(request, "Index.html", {"Url" : ini.Url, "Language" : ini.AceSetting[Lang], "Select" : Select, "csrf_token" : csrf(request)['csrf_token']})
    
@csrf_exempt
def Login(request):
    return render(request, "Login.html", {"Url" : ini.Url, "csrf_token" : csrf(request)['csrf_token'] })
