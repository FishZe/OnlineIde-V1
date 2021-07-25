import os
import json
import random
import string
import hashlib
import requests
import shutil

from urllib import parse
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from . import ini

def RandStr():
    seed = "abcdefghijklmnopqrstuvwxyz0123456789"
    sa = []
    for i in range(32):
      sa.append(random.choice(seed))
    return "".join(sa)
    
    
def DeleteCaseFile(TestCaseRode, TestCaseId):
    shutil.rmtree(TestCaseRode + TestCaseId)
    
def WriteCaseFile(TestCaseRode, CaseData):
    
    TestCases = {}
    TestCaseId = RandStr()
    
    while os.path.exists(TestCaseRode + TestCaseId):
        TestCaseId = RandStr()
    os.makedirs(TestCaseRode + TestCaseId)
    
    for i in range(1, int(CaseData["Num"]) + 1):
        InputFile = open(TestCaseRode + TestCaseId + '/' + str(i) + '.in', mode = 'w')
        InputFile.write(CaseData[str(i)]["Input"])
        InputFile.close()
        
        OutputFile = open(TestCaseRode + TestCaseId + '/' + str(i) + '.out', mode = 'w')
        OutputFile.write(CaseData[str(i)]["Output"])
        OutputFile.close()
        
        OutputFile = open(TestCaseRode + TestCaseId + '/' + str(i) + '.out', mode = 'rb')
        OutputFileMD5 = hashlib.md5(OutputFile.read()).hexdigest()
        OutputFile.close()
        
        TestCases[str(i)] = {
            "stripped_output_md5": OutputFileMD5,
            "output_size": os.path.getsize(TestCaseRode + TestCaseId + '/' + str(i) + '.out'),
            "input_name": str(i) + ".in",
            "input_size": os.path.getsize(TestCaseRode + TestCaseId + '/' + str(i) + '.in'),
            "output_name": str(i) + ".out"
        }
        
    Info = { "spj": False, "test_cases": TestCases}
    
    InfoFile = open(TestCaseRode + TestCaseId + '/info', mode = "w")
    InfoFile.write(json.dumps(Info, indent = 4))
    InfoFile.close
    
    return TestCaseId
    
    
def PostCompile(JudgeUrl, XJudgeServerToken, Code, Time, Memory, Lan, TestCaseRode, TestData):
    TestCaseId = WriteCaseFile(TestCaseRode, TestData)
    
    Data = {"headers" : {"X-Judge-Server-Token" : hashlib.sha256(XJudgeServerToken.encode("utf-8")).hexdigest(), "Content-Type" : "application/json"}}
    Data["json"] = {
        "src": Code,
    	"language_config": ini.Language[Lan],
    	"max_cpu_time": int(Time),
    	"max_memory": (int(Memory) * 1024 * 1024),
    	"test_case_id": TestCaseId,
    	"output": True
    }
    
    
    Result = requests.post(JudgeUrl, **Data).json()
    
    shutil.rmtree(TestCaseRode + TestCaseId)
    
    return Result
