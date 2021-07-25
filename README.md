# OnlineIde

Online ide 在线编辑/编译器  


Written by YuFengze 2021/07/26 00:03


Demo: https://ide.yufengze.org

嗝，刚写的没保存全丢了，手残

OIer一只，英语不行，中文也不多好，将就看吧

由于要打竞赛，有个OnlineIde会很方便，洛谷喜欢炸也不方便，索性就自己写了一个

主业C++，html+css+js全是自学的，python自己摸索的，语法开发啥的都不会，随便写的
如果出现了if(){}或者xxx;的奇怪场景，千万不要惊讶，请高呼 “理解万岁！！”

框架是django，不懂的去看文档，很简单，易上手

判题机是青岛大学的oj，如果想用我的ide还需要clone一个qingdaou，那个比我这个还容易安装，直接几行代码就解决了

前端编辑器是Ace的，也很容易好用

为了防止我的ide被别人大量使用，就随便写了个登录，挂着数据库，数据库我用的mysql和我的博客一起更便于管理，当然你也可以用自带的数据库

为了防止把服务器搞坏，我做了个“联机”，其实就是多个判题机，所以你可以把这个项目同步到好几个服务器上并只开启一个服务器的前端服务，其余几个只是判题

毕竟我的服务器上有好几个网站和一堆项目，卡掉了就完犊子了


数据库就一个表，id, name, email, password(md5(32)), number


前面几个不多解释，最后一个number本打算做一个剩余运行次数来限制一些访客的，咕了


一共3个app，分别是web,api,run

    
    web负责前端，就是index和login这俩小玩意儿

    api管登录和运行任务的分发，有一个queue，可以平均负载

    run就是写样例和oj交互，这没啥
    

食用方法：

    开盖即食（误）

    把三个app下的ini.py改咯

    把OnlineIde下的setting.py改咯

    开启服务就好了
    
    python manage.py migrate
    python manage.py runserver 0.0.0.0:port

    

这边建议顺便打开nginx的反向代理和缓存，更爽


TODO(咕)：

    前端代码运行频率限制

    前端改的好看一点

    前端代码要更整洁一些

    增加一个代码分享和储存功能

完
