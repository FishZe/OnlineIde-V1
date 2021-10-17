## demo: [YFZ-Ide](https://ide.yufengze.org)


### 你可以一步安装：
(使用的是apt，还没有做yum的支持)

```
wget https://www.yufengze.org/download/onlineide/install.cn.sh && sh install.cn.sh
```

### 你也可以手动安装：

依赖：git docker.io nodejs python3 python3-pip npm

python库： django apscheduler django-cors-headers

需要手动将编辑器通过npm安装到django的static目录下

#### 示例代码：
不支持apt的小伙伴请手动切换yum
```
sudo apt-get update && apt-get install -y git docker.io nodejs python3 python3-pip npm
sudo git clone https://hub.fastgit.org/YuFengZe/OnlineIde.git
sudo docker pull yufengze/onlineide
sudo nohup docker run --network host -v $(pwd)/OnlineIde/Runner:/Project/CodeRunner --privileged yufengze/onlineide &
sudo pip3 install --trusted-host https://pypi.doubanio.com/simple/ django apscheduler django-cors-headers
sudo npm install --prefix $(pwd)/OnlineIde/OnlineIde/static monaco-editor
sudo python3 OnlineIde/OnlineIde/manage.py migrate && python3 OnlineIde/OnlineIde/manage.py runserver 0.0.0.0:8000
```
