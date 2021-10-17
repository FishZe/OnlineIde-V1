import os
import json
import base64
import hashlib
import requests
import urllib.parse
from apscheduler.schedulers.background import BackgroundScheduler


from flask import Flask
from flask import request


from main import *
import ini

app = Flask(__name__)

# 一个小小滴示例
# a little case:
'''
{
    "Name" : "main.cpp",
    "CompileName" : "main",
    "Language" : "cpp",
    "Memory" : 128 * 1024 * 1024 * 1024,
    "Time" : 3000,
    "Input" : "Hello world!",
    "Code" : "%23include%20%3Ciostream%3E%0A%23include%20%3Cstring%3E%0Ausing%20namespace%20std%3B%0A%0Aint%20main%28%29%7B%0A%20%20%20%20string%20s%3B%0A%20%20%20%20cin%20%3E%3E%20s%3B%0A%20%20%20%20cout%20%3C%3C%20s%3B%0A%20%20%20%20return%200%3B%0A%7D",
    "CompileCmd" : ["/usr/bin/g++", "main.cpp", "-o", "main"], 
    "RunCmd" : ["main"],
}

'''

Connected = False
Id = ""
Key = ""

def Connect():

    global Connected
    global Id
    global Key

    if not Connected:
        Res = ''
        try:
            
            Data = json.dumps({"Port": ini.Port, "Token": hashlib.sha256(ini.Token.encode('utf-8')).hexdigest(), "Name": ini.Name})

            Res = json.loads(requests.post(ini.OnlineIdeUrl + '/connect', Data).text)

            if Res['State'] == "Connect":
                Connected = True
                Id = Res['Id']
                Key = Res['Key']

        except:

            Connected = False
    
    else:

        try: 

            Data = json.dumps({"Id": Id, "Token": hashlib.sha256(ini.Token.encode('utf-8')).hexdigest()})

            Ans = requests.post(ini.OnlineIdeUrl + '/ping', Data).text

            if Ans != "pong!":
                Connected = False
                
        except:
            Connected = False



def CompileData(Req):

    Data = {"headers" : {"Content-type" : "application/json"}}
    Data["json"] = {
        "cmd": [{
            "args": Req['CompileCmd'],
            "env": ["PATH=/usr/bin:/bin:/usr/local/node, GOPATH=/w, GOCACHE=/tmp"],
            "files": [{
                "content": Req['Input'],
            }, {
                "name": "stdout",
                "max": 10240
            }, {
                "name": "stderr",
                "max": 10240
            }],
            "cpuLimit": 20000 * 1000000,
            "memoryLimit": Req['Memory'],
            "procLimit": 50,
            "copyIn": {
                Req['Name']: {
                    "content": base64.b64decode(Req['Code']).decode("utf-8"),
                }
            },
            "copyOut": ["stdout", "stderr"],
            "copyOutCached": [Req['Name'], Req['CompileName']],
            "copyOutDir": "1"
        }]
    }
    return Data

def RunData(CompileAns, Req):

    Data = {"headers" : {"Content-type" : "application/json"}}
    Data["json"] = {
        "cmd": [{
            "args": Req['RunCmd'],
            "env": ["PATH=/usr/bin:/bin,GOPATH=/w,GOCACHE=/tmp"],
            "files": [{
                "content": Req['Input'],
            }, {
                "name": "stdout",
                "max": 10240
            }, {
                "name": "stderr",
                "max": 10240
            }],
            "cpuLimit": Req['Time'] * 1000000,
            "memoryLimit": Req['Memory'],
            "procLimit": 50,
            "strictMemoryLimit": False,
            "copyIn": {
                Req['CompileName']: {
                    "fileId": CompileAns['fileIds'][Req['CompileName']]
                },
            }
        }]
    }
    return Data
    

def CodeRunner(Req):

    CompileAns =  json.loads((requests.post("http://127.0.0.1:5050/run", **CompileData(Req))).text[1:-2])

    Runans = {}

    if CompileAns['status'] == "Accepted":

        PostAns =  json.loads((requests.post("http://127.0.0.1:5050/run", **RunData(CompileAns, Req))).text[1:-2])
        
        if PostAns['status'] == "Accepted":

            RunAns = {"error": 0, 
                      "cpu_time": round(PostAns['time'] / 1000000, 3), 
                      "Time": round(PostAns['runTime'] / 1000000, 3),
                      "memory": PostAns['memory'], 
                      "Output": PostAns['files']['stdout']}

        elif PostAns['status'] == "Nonzero Exit Status":

            RunAns = {"error": 3, "Output": PostAns['files']['stderr'] }

        elif PostAns['status'] == "Time Limit Exceeded":

            RunAns = {"error": 4, 'Output': PostAns['files']['stdout']}
        
        elif PostAns['status'] == "Memory Limit Exceeded":

            RunAns = {"error": 5, 'Output': PostAns['files']['stdout']}

        else:
            
            RunAns = {"error": 2}


    elif CompileAns['status'] == "Nonzero Exit Status":
        
        RunAns = {"error": 1, "Output": CompileAns['files']['stderr'] + CompileAns['files']['stdout']}
    
    else:

        RunAns = {"error": 2}

    try:
        os.system("rm -f ./Code/" + CompileAns['fileIds'][Req['Name']])
        os.system("rm -f ./Code/" + CompileAns['fileIds'][Req['CompileName']])
    except:
        os.system("")

    return RunAns



@app.route('/accept', methods=["POST"])
def accept():
    
    global Key

    Req = json.loads(request.data)
    
    
    if Req["Key"] != hashlib.sha256(Key.encode('utf-8')).hexdigest():
        return {"error" : 2, "Output": "错误！"}

    Ans = CodeRunner(Req)
    
    return Ans


if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(Connect, 'interval', seconds=5)
    scheduler.start()
    app.run(host = "0.0.0.0", port = ini.Port, debug = False)
    
