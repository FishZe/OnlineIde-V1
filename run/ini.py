#全局变量 请自行更改设置

OpenJudge = True;
#开启判题

TestCaseRode = "/home/OnlineJudgeDeploy/data/backend/test_case/"
#本服务器的样例地址

JudgesUrl = "http://172.18.0.3:8080/judge"
#oj判题机的地址
#不知道的到oj的后台查看

XJudgeServerTokens = 'b824cecedb22b06c3883b1f1dd9dd3150608fc24f8d0c16b0f85af8c8c761667'
#本服务器的判题机的token

JudgeServersPassword = "12345"

SupportLanguages = {'cpp', 'c', 'java', 'python2', 'python3', 'go'}
#支持的语言

Language = {}
Language['cpp'] = {
    "compile": {
        "src_name": "main.cpp",
        "exe_name": "main",
        "max_cpu_time": 3000,
        "max_real_time": 5000,
        "max_memory": 134217728,
        "compile_command": "/usr/bin/g++ -DONLINE_JUDGE -O -w -fmax-errors=3 -std=c++14 {src_path} -lm -o {exe_path}"
    },
    "run": {
        "command": "{exe_path}",
        "seccomp_rule": "c_cpp",
        "env": ["LANG=en_US.UTF-8", "LANGUAGE=en_US:en", "LC_ALL=en_US.UTF-8"]
    }
}
Language['c'] = {
    "compile": {
        "src_name": "main.c",
        "exe_name": "main",
        "max_cpu_time": 3000,
        "max_real_time": 10000,
        "max_memory": 256 * 1024 * 1024,
        "compile_command": "/usr/bin/gcc -DONLINE_JUDGE -O2 -w -fmax-errors=3 -std=c11 {src_path} -lm -o {exe_path}",
    },
    "run": {
        "command": "{exe_path}",
        "seccomp_rule": "c_cpp",
        "env": ["LANG=en_US.UTF-8", "LANGUAGE=en_US:en", "LC_ALL=en_US.UTF-8"]
    }   
}
Language['java'] = {
    "compile": {
        "src_name": "Main.java",
        "exe_name": "Main",
        "max_cpu_time": 5000,
        "max_real_time": 10000,
        "max_memory": -1,
        "compile_command": "/usr/bin/javac {src_path} -d {exe_dir} -encoding UTF8"
    },
    "run": {
        "command": "/usr/bin/java -cp {exe_dir} -XX:MaxRAM={max_memory}k -Djava.security.manager -Dfile.encoding=UTF-8 "
                   "-Djava.security.policy==/etc/java_policy -Djava.awt.headless=true Main",
        "seccomp_rule": None,
        "env": ["LANG=en_US.UTF-8", "LANGUAGE=en_US:en", "LC_ALL=en_US.UTF-8"],
        "memory_limit_check_only": 1
    }
}
Language['python2'] = {
    "compile": {
        "src_name": "solution.py",
        "exe_name": "solution.pyc",
        "max_cpu_time": 3000,
        "max_real_time": 10000,
        "max_memory": 128 * 1024 * 1024,
        "compile_command": "/usr/bin/python -m py_compile {src_path}",
    },
    "run": {
        "command": "/usr/bin/python {exe_path}",
        "seccomp_rule": "general",
        "env": ["LANG=en_US.UTF-8", "LANGUAGE=en_US:en", "LC_ALL=en_US.UTF-8"]
    }
}
Language['python3'] = {
    "compile": {
        "src_name": "solution.py",
        "exe_name": "__pycache__/solution.cpython-36.pyc",
        "max_cpu_time": 3000,
        "max_real_time": 10000,
        "max_memory": 128 * 1024 * 1024,
        "compile_command": "/usr/bin/python3 -m py_compile {src_path}",
    },
    "run": {
        "command": "/usr/bin/python3 {exe_path}",
        "seccomp_rule": "general",
        "env": ["LANG=en_US.UTF-8", "LANGUAGE=en_US:en", "LC_ALL=en_US.UTF-8", "PYTHONIOENCODING=utf-8"]
    }
}
Language['go'] = {
    "compile": {
        "src_name": "main.go",
        "exe_name": "main",
        "max_cpu_time": 3000,
        "max_real_time": 5000,
        "max_memory": 1024 * 1024 * 1024,
        "compile_command": "/usr/bin/go build -o {exe_path} {src_path}",
        "env": ["GOCACHE=/tmp"]
    },
    "run": {
        "command": "{exe_path}",
        "seccomp_rule": "",
        # 降低内存占用
        "env": ["GODEBUG=madvdontneed=1", "LANG=en_US.UTF-8", "LANGUAGE=en_US:en", "LC_ALL=en_US.UTF-8"],
        "memory_limit_check_only": 1
    }
}
