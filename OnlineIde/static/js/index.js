var OnlineIdeHeight = document.documentElement.clientHeight;
var OnlineIdeWidth = document.documentElement.clientWidth;
var Languages = ["C++ 98", "C++ 11", "C++ 14", "C++ 17", "C", "Python 2", "Python 3", "Java", "JavaScript", "PHP", "Go", "TypeScript", "Pascal", "Haskell", "Rust", "Ruby", "Csharp", "Perl", "文言"];
var LanguagesConfig = ['cpp98', 'cpp11', 'cpp14', 'cpp17', 'c', 'python', 'python3', 'java', "javascript", "php", "go", "typescript", "pascal", "haskell", "rust", "ruby", "csharp", "perl", "wenyan"];
var EditorConfig = ['cpp', 'cpp', 'cpp', 'cpp', 'c', 'python', 'python', 'java', "javascript", "php", "go", "typescript", "pascal", "haskell", "rust", "csharp", "perl", "txt"];
		    
var NowSelectedLanguage = 0;

document.getElementById("Selected").innerHTML = Languages[NowSelectedLanguage];

function Init(){
    document.getElementById("PageSelect").style.height = OnlineIdeHeight + 'px';
    document.getElementById("CodeRunner").style.width = document.getElementById("CodeEditor").style.width = document.getElementById("CodeCommand").style.width = OnlineIdeWidth - 50 + 'px';
    document.getElementById("CodeEditor").style.height = (OnlineIdeHeight - 70) * 0.75 + 'px';
    document.getElementById("CodeRunner").style.height = (OnlineIdeHeight - 70) * 0.25 + 35 + 'px';
    document.getElementById('ChangeLanguage').style.display = "none";
    document.getElementById("OutputEditor").style.width = document.getElementById("InputEditor").style.width = document.getElementById("Input").style.width = 
    document.getElementById("Output").style.width = (OnlineIdeWidth - 80) / 2 + 'px';
    document.getElementById("OutputEditor").style.height = document.getElementById("InputEditor").style.height = (OnlineIdeHeight - 70) * 0.25 - 5 + 'px'; 
    document.getElementById("Question").style.top = (OnlineIdeHeight - 100) / 2 - 100 + 'px';
    document.getElementById("Question").style.left = (OnlineIdeWidth - 300) / 2 + 'px';
    document.getElementById("Barrier").style.height = OnlineIdeHeight + 'px';
    document.getElementById("Barrier").style.width = OnlineIdeWidth + 'px';
    document.getElementById('Barrier').style.display = "none";
    document.getElementById('Question').style.display = "none";
}


window.onresize=function(){ 
    Init();
}

Init();

var CodeEditor;
var InputEditor;
var OutputEditor;

var Get = 0;

function InitCodeEditor(Language){
    require.config({ paths: { vs: './static/node_modules/monaco-editor/min/vs' } });
    require(['vs/editor/editor.main'], function () {
        CodeEditor = monaco.editor.create(document.getElementById('CodeEditor'), {
            value: [''].join('\n'),
            language: Language,
            theme: "vs-dark",
            automaticLayout: true,
            availableLanguages: {'*':'zh-cn'}
        });
    });
    

}
InitCodeEditor(EditorConfig[0]);


    function InitInputEditor(){
    require.config({ paths: { vs: './static/node_modules/monaco-editor/min/vs' } });
    require(['vs/editor/editor.main'], function () {
        InputEditor = monaco.editor.create(document.getElementById('InputEditor'), {
            language: 'text',
            theme: "vs-dark",
            automaticLayout: true,
            minimap: {
                enabled: false,
            },
        });
    });
    }
    InitInputEditor();
    
    function InitOutputEditor(){
    require.config({ paths: { vs: './static/node_modules/monaco-editor/min/vs' } });
    require(['vs/editor/editor.main'], function () {
        OutputEditor = monaco.editor.create(document.getElementById('OutputEditor'), {
            language: 'text',
            theme: "vs-dark",
            automaticLayout: true,
            readOnly: true,
            minimap: {
                enabled: false,
            },
        });
    });
    }
    InitOutputEditor();


function ChangeLanguage(){
    if(document.getElementById('ChangeLanguage').style.display === 'block'){
        document.getElementById('ChangeLanguage').style.display = "none";
        return;
    }
    console.log("1");
    document.getElementById('ChangeLanguage').style.display = "block";
}
function SelectLanguage(obj){
    NowSelectedLanguage = obj.value;
    document.getElementById("Selected").innerHTML = Languages[obj.value]; 
    CodeEditor.dispose();
    InitCodeEditor(EditorConfig[obj.value]);
    ChangeLanguage();
}

$(document).mouseup(function (e) {
    var ChangeLanguage = $("#ChangeLanguage"); 
    if (!ChangeLanguage.is(e.target) && ChangeLanguage.has(e.target).length === 0) {
        if(document.getElementById('ChangeLanguage').style.display == "block"){
            document.getElementById('ChangeLanguage').style.display = "none";
        } 
    }
});

window.onload = function () {
    var Border = document.getElementById('Border');
    var CodeRunner = document.getElementById('CodeRunner');
    var CodeEditor = document.getElementById("CodeEditor");
    var InputEditor = document.getElementById("InputEditor");
    var OutputEditor = document.getElementById("OutputEditor");
    
    var DisY = 0;
    var CodeRunnerHeight = 0; 
    var CodeEditorHeight = 0;
    var IOEditorHeight = 0;
    
    Border.onmousedown = function (ev) {
        var ev = ev || window.event;
        
        DisY = ev.clientY; 
        CodeRunnerHeight = CodeRunner.offsetHeight;
        CodeEditorHeight = CodeEditor.offsetHeight;
        IOEditorHeight = InputEditor.offsetHeight;
        
        document.onmousemove = function (ev) {
            var ev = ev || window.event;

            var CodeRunnerChangedHeight = - ev.clientY + DisY + CodeRunnerHeight;
            var IOEditorChangedHeight = - ev.clientY + DisY + IOEditorHeight;
            var CodeEditorChangedHeight = ev.clientY - DisY + CodeEditorHeight;
            
            if(CodeRunnerChangedHeight + CodeEditorChangedHeight > OnlineIdeHeight || CodeRunnerChangedHeight < 80 || CodeEditorChangedHeight < 50){
                return;    
            }

            CodeRunner.style.height = CodeRunnerChangedHeight +'px';
            CodeEditor.style.height = CodeEditorChangedHeight + 'px';
            InputEditor.style.height = OutputEditor.style.height =IOEditorChangedHeight + 'px';
        }
        document.onmouseup = function () {
            document.onmousemove = null;
            document.onmouseup = null;
        }
    }
}

function NotClearCode(){
    document.getElementById('Barrier').style.display = "none";
    document.getElementById('Question').style.display = "none";
}

function ClearCode(){
    NotClearCode();
    CodeEditor.setValue('');
}

function ClickClearCode(){
    document.getElementById('Barrier').style.display = "block";
    document.getElementById('Question').style.display = "block";
    document.getElementById("RequestWords").innerHTML = "确认清空代码吗?";
    document.getElementById('No').onclick = function(){NotClearCode()};
    document.getElementById('Yes').onclick = function(){ClearCode()};
}

function CodeEmpty(){
    document.getElementById('No').style.display = "block";
    document.getElementById('Barrier').style.display = "none";
    document.getElementById('Question').style.display = "none";
    
}

function GetAns(text){
    Get += 1;
    if(Get >= 30){
        OutputEditor.setValue("Out of Time\n");
        return;
    }
    OutputEditor.setValue("Running......\n");
    var xhr = new XMLHttpRequest();
    xhr.open("POST",  "getans", true);
    xhr.setRequestHeader('X-CSRFtoken', csrf_token );
    xhr.onreadystatechange = function(){
        var XMLHttpReq = xhr;
        if (XMLHttpReq.readyState == 4 && XMLHttpReq.status == 200) {
                var Ans = XMLHttpReq.responseText;
                console.log(Ans);
                if(Ans == "no"){
                    setTimeout("GetAns('" + text + "')", 500)
                } else {
                    OutputEditor.setValue(Ans);
                }
            }
    };
    xhr.send(text);
}

function RunCode(){
    if(CodeEditor.getValue() == ""){
        document.getElementById('Barrier').style.display = "block";
        document.getElementById('Question').style.display = "block";
        document.getElementById('No').style.display = "none";
        document.getElementById("RequestWords").innerHTML = "代码不能为空！";
        document.getElementById('Yes').onclick = function(){CodeEmpty()};
        return;
    }
    var Code = InputEditor.getValue();
    OutputEditor.setValue("Submiting......\n");
    var postData = {
        "Language" : LanguagesConfig[NowSelectedLanguage],
        "Input" : InputEditor.getValue(),
        "Code" : window.btoa(CodeEditor.getValue()),
    };
    postData = JSON.stringify(postData);
    var xhr = new XMLHttpRequest();
    xhr.open("POST",  "runcode", true);
    xhr.setRequestHeader('X-CSRFtoken', csrf_token );
    xhr.onreadystatechange = function(){
        var XMLHttpReq = xhr;
        if (XMLHttpReq.readyState == 4 && XMLHttpReq.status == 200) {
                var text = XMLHttpReq.responseText;
                Get = 0;
                GetAns(text);
            }
    };
    xhr.send(postData);
}