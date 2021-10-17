import time
import json
import queue
import random
import hashlib
import threading
import requests

from apscheduler.schedulers.background import BackgroundScheduler

from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from . import ini


ServersQueue = queue.Queue()
Serverslist = []
Answer = {}
    
def RandStr():
    Seed = "abcdefghijklmnopqrstuvwxyz0123456789"
    Str = []
    for i in range(32):
      Str.append(random.choice(Seed))
    return "".join(Str)
        
def CheckServers():
    global Serverslist

    if len(Serverslist) == 0:
        return

    i = 0
    lens = len(Serverslist)

    while i < lens:
        if time.time() - Serverslist[i]['LastTime'] >= 10:
            Serverslist.pop(i)
            print("删除！")
            i -= 1
            lens -= 1
            
        i += 1
        

Check = BackgroundScheduler()
Check.add_job(CheckServers, 'interval', seconds = 10)
Check.start()

def Runner(Req, x):
    while ServersQueue.empty():
        time.sleep(0.1)
                    
    NowServer = ServersQueue.get()

    if NowServer >= len(Serverslist):
        Run = threading.Timer(0, Runner, (Req, 0))
        Run.start()
        return

    Req["Key"] = hashlib.sha256(Serverslist[NowServer]["Key"].encode('utf-8')).hexdigest()
    
    
    Data = {"headers" : {"Content-type" : "application/json"}}
    Data["json"] = Req
    
    try:
        Ans = json.loads((requests.post(Serverslist[NowServer]['ServerUrl'] + '/accept', **Data)).text)
    except requests.exceptions.ConnectionError:
        Ans = {"error" : 2, "Output": "无法连接CodeRunner", "Id": Req['Id'], "Judger": NowServer}
    except requests.exceptions.ConnectTimeout:
        Ans = {"error" : 2, "Output": "CodeRunner连接超时", "Id": Req['Id'], "Judger": NowServer}
    except requests.exceptions.ProxyError:
        Ans = {"error" : 2, "Output": "请联系管理员检查网络环境", "Id": Req['Id'], "Judger": NowServer}
    
    Ans['Runner'] = NowServer
    
    Answer[Req['Id']] = Ans
    
    
    ServersQueue.put(NowServer)
    
@require_http_methods(["POST"])
def GetAns(request):
    Req = request.body.decode("utf-8")
    
    if Req in Answer:
        Res = Answer[Req]
        Ans = ""
        
        if Res['error'] == 1:
            Ans = "Compile Error! region: " + Serverslist[Res['Runner']]["Name"] + "\n" + Res['Output']
        elif Res['error'] == 2:
            Ans = "服务器错误! \n "
        elif Res['error'] == 3:
            Ans = "运行错误!  region: " + Serverslist[Res['Runner']]["Name"] + "\n" + Res['Output']
        elif Res['error'] == 4:
            Ans = "TLE!  region: " + Serverslist[Res['Runner']]["Name"] + "\n" + Res['Output']
        elif Res['error'] == 5:
            Ans = "MLE!  region: " + Serverslist[Res['Runner']]["Name"] + "\n" + Res['Output']
        else :
            Ans = "Run Time: " + str(Res['cpu_time']) + "ms   Memory: " + str(round(Res['memory'] / 1024 / 1024 , 3)) + "MB   region: " + Serverslist[Res['Runner']]["Name"] + "\n" + Res['Output']

        return HttpResponse(Ans)
        
    else:
        return HttpResponse("no")

@require_http_methods(["POST"])
def RunCode(request):
    Req = json.loads(request.body)
        
    Run = {
        'Id': RandStr(),
        'Language': Req['Language'],
        "Name": ini.Language[Req['Language']]["Name"],
        "CompileName" : ini.Language[Req['Language']]["CompileName"],
        "Memory": 256 * 1024 * 1024,
        "Time": 3000,
        "Input": Req['Input'],
        "Code": Req['Code'],
        "RunCmd" : ini.Language[Req['Language']]["RunCmd"],
        "CompileCmd" : ini.Language[Req['Language']]["CompileCmd"], 
    }
    
    timer = threading.Timer(0, Runner, (Run, 0))
    timer.start()

    return HttpResponse(Run['Id'])
    
@require_http_methods(["GET"])
def Index(request):

    return render(request, "Index.html", {"csrf_token" : csrf(request)['csrf_token']})


#如果需要压力测试，请将urls中的注释删去
#默认关闭 防止被他人使用
@csrf_exempt
@require_http_methods(["GET"])
def Wrk(request):

    Run = {
        'Id': RandStr(),
        'Language': "cpp14",
        "Name": ini.Language["cpp14"]["Name"],
        "CompileName" : ini.Language["cpp14"]["CompileName"],
        "Memory": 256 * 1024 * 1024,
        "Time": 3000,
        "Input": "1 2",
        "Code": "using%20namespace%20std%3B%0D%0A%0D%0Aint%20main%28%29%7B%0D%0A%20%20%20%20double%20a%20%3D%201.555%2C%20b%20%3D%201.666%3B%0D%0A%20%20%20%20int%20times1%20%3D%201e5%2C%20times2%20%3D%204e4%3B%0D%0A%20%20%20%20for%28int%20i%20%3D%200%3B%20i%20%3C%20times1%3B%20i++%29%7B%0D%0A%20%20%20%20%20%20%20%20for%28int%20j%20%3D%200%3B%20j%20%3C%20times2%3B%20j++%29%7B%0D%0A%20%20%20%20%20%20%20%20%20%20%20%20a%20*%3D%20b%3B%0D%0A%20%20%20%20%20%20%20%20%7D%0D%0A%20%20%20%20%7D%0D%0A%20%20%20%20return%200%3B%0D%0A%7D%0D%0A%0D%0A",
        "RunCmd" : ini.Language["cpp14"]["RunCmd"],
        "CompileCmd" : ini.Language["cpp14"]["CompileCmd"], 
    }

    
    Runner(Run, 0)
    
    return HttpResponse(json.dumps(Answer[Run["Id"]]))
    

@csrf_exempt
@require_http_methods(["POST"])
def Connect(request):
        
    global Serverslist

    Req = json.loads(request.body)

    if Req['Token'] != hashlib.sha256(ini.Token.encode('utf-8')).hexdigest():
        return HttpResponse("No!")

    ServerUrl = "http://" + str(request.META.get('REMOTE_ADDR')) + ':' + str(Req['Port'])
    ServerId = RandStr()

    ServersQueue.put(len(Serverslist))

    NowServer = {"ServerUrl": ServerUrl, 
                 "LastTime": time.time(), 
                 "Id": ServerId,
                 "Key": RandStr(),
                 "Name": Req['Name'] }

    Serverslist.append(NowServer)

    return HttpResponse(json.dumps({"Id": ServerId, "State": "Connect", "Key": NowServer['Key']}))

@csrf_exempt
@require_http_methods(["POST"])
def Ping(request):

    Found = False

    Req = json.loads(request.body)

    if Req['Token'] != hashlib.sha256(ini.Token.encode('utf-8')).hexdigest():
        return HttpResponse("No!")

    for i in Serverslist:
        if i['Id'] == str(Req['Id']):
            Found = True
            i['LastTime'] = time.time()
            break
        

    if not Found:
        return HttpResponse("No!")

    return HttpResponse("pong!")

@require_http_methods(["GET"])
def RunnerInfo(request):
    Ans = "<table>"
    for i in Serverslist:
        Ans += '<tr><th>' + i['ServerUrl'] + '</th><th>' + time.asctime(time.localtime(i['LastTime']))  + '</th><th>' + i["Name"] + '</th></tr>'
    Ans += "</table>"
    return HttpResponse(Ans)
    
def NotFound(request,  template_name = '404.html'):
    
    return render(request, "404.html")


