Token = "ABC"


Language = {}

Language['cpp98'] = {
    "Name" : "main.cpp",
    "CompileName" : "main",
    "RunCmd" : ["main"],
    "CompileCmd" : ["/usr/bin/g++", "-O", "-w", "-fmax-errors=3", "-std=c++98", "main.cpp", "-lm", "-o", "main"], 
}


Language['cpp11'] = {
    "Name" : "main.cpp",
    "CompileName" : "main",
    "RunCmd" : ["main"],
    "CompileCmd" : ["/usr/bin/g++", "-O", "-w", "-fmax-errors=3", "-std=c++11", "main.cpp", "-lm", "-o", "main"], 
}



Language['cpp14'] = {
    "Name" : "main.cpp",
    "CompileName" : "main",
    "RunCmd" : ["main"],
    "CompileCmd" : ["/usr/bin/g++", "-O", "-w", "-fmax-errors=3", "-std=c++14", "main.cpp", "-lm", "-o", "main"], 
}


Language['cpp17'] = {
    "Name" : "main.cpp",
    "CompileName" : "main",
    "RunCmd" : ["main"],
    "CompileCmd" : ["/usr/bin/g++", "-O", "-w", "-fmax-errors=3", "-std=c++17", "main.cpp", "-lm", "-o", "main"], 
}


Language['c'] = {
    "Name" : "main.c",
    "CompileName" : "main",
    "RunCmd" : ["main"],
    "CompileCmd" : ["/usr/bin/gcc", "-O", "-w", "-fmax-errors=3", "-std=c++17", "main.c", "-lm", "-o", "main"], 
}


Language['python3'] = {
    "Name" : "solution.py",
    "CompileName" : "solution.pyc",
    "RunCmd" : ["/usr/bin/python3", "solution.pyc"],
    "CompileCmd" : ["/usr/bin/python3", "-c", "import py_compile; py_compile.compile('solution.py', 'solution.pyc', doraise=True)"], 
}

Language['python'] = {
    "Name" : "solution.py",
    "CompileName" : "solution.pyc",
    "RunCmd" : ["/usr/bin/python2", "solution.pyc"],
    "CompileCmd" : ["/usr/bin/python2", "-c", "import py_compile; py_compile.compile('solution.py', 'solution.pyc', doraise=True)"], 
}

Language['java'] = {
    "Name" : "Main.java",
    "CompileName" : "Main.class",
    "RunCmd" : ["/usr/bin/java", "Main"],
    "CompileCmd" : ["/usr/bin/javac", "Main.java"], 
}

Language['javascript'] = {
    "Name" : "main.js",
    "CompileName" : "main.js",
    "RunCmd" : ["/usr/bin/node", "main.js"],
    "CompileCmd" : ["/bin/echo", "compile"], 
}

Language['php'] = {
    "Name" : "main.php",
    "CompileName" : "main.php",
    "RunCmd" : ["/usr/bin/php", "main.php"],
    "CompileCmd" : ["/bin/echo", "compiled"], 
}

Language['go'] = {
    "Name" : "solution.go",
    "CompileName" : "solution",
    "RunCmd" : ["solution"],
    "CompileCmd" : ["/usr/local/go/bin/go", "build", "-o", "solution", "solution.go"], 
}

Language['typescript'] = {
    "Name" : "main.ts",
    "CompileName" : "main.js",
    "RunCmd" : ["/usr/bin/node", "main.js"],
    "CompileCmd" : ["/usr/local/lib/node_modules/typescript/bin/tsc", "--outFile", "main.js", "main.ts"], 
}

Language['pascal'] = {
    "Name" : "main.pas",
    "CompileName" : "main",
    "RunCmd" : ["main"],
    "CompileCmd" : ["/usr/bin/fpc", "-O2", "main.pas"], 
}

Language['haskell'] = {
    "Name" : "main.hs",
    "CompileName" : "main",
    "RunCmd" : ["main"],
    "CompileCmd" : ["/usr/bin/ghc", "-o", "main", "main.hs"], 
}

Language['rust'] = {
    "Name" : "main.rs",
    "CompileName" : "main",
    "RunCmd" : ["main"],
    "CompileCmd" : ["/usr/bin/rustc", "-o", "main", "main.rs"], 
}

Language['ruby'] = {
    "Name" : "main.rb",
    "CompileName" : "main.rb",
    "RunCmd" : ["/usr/bin/ruby", "main.rb"],
    "CompileCmd" : ["/bin/echo", "compiled"], 
}

Language['csharp'] = {
    "Name" : "main.cs",
    "CompileName" : "main",
    "RunCmd" : ["/usr/bin/mono", "main"],
    "CompileCmd" : ["/usr/bin/mcs", "-optimize+", "-out:main", "main.cs"], 
}

Language['perl'] = {
    "Name" : "main.pl",
    "CompileName" : "main.pl",
    "RunCmd" : ["/usr/bin/perl", "main.pl"],
    "CompileCmd" : ["/bin/echo", "compiled"], 
}

Language['wenyan'] = {
    "Name" : "main.wy",
    "CompileName" : "main.wy",
    "RunCmd" : ["/usr/local/bin/wenyan", "main.wy", "-o", "main.js"],
    "CompileCmd" : ["/bin/echo", "compile"], 
}
