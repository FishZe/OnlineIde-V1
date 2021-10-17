FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive

LABEL author=yufengze

USER root

# Run sed -E -i -e 's/(archive|ports).ubuntu.com/mirrors.tuna.tsinghua.edu.cn/g' -e '/security.ubuntu.com/d' /etc/apt/sources.list

RUN apt-get update && apt-get install -y wget python python3 python-pkg-resources python3-pkg-resources software-properties-common git libtool python-dev python3-pip nodejs npm 

# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -I --no-cache-dir psutil gunicorn flask requests idna apscheduler

RUN npm -g install typescript && npm i --save-dev @types/node && npm install -g @wenyan/cli

RUN pip3 install -I --no-cache-dir psutil gunicorn flask requests idna apscheduler

RUN add-apt-repository ppa:openjdk-r/ppa && \
    add-apt-repository ppa:ubuntu-toolchain-r/test && \
    add-apt-repository ppa:ondrej/php && \
    apt-get update && apt-get install -y openjdk-11-jdk gcc-9 g++-9 php fp-compiler ghc rustc ruby mono-mcs perl && \
    update-alternatives --install  /usr/bin/gcc gcc /usr/bin/gcc-9 40 && \
    update-alternatives --install  /usr/bin/g++ g++ /usr/bin/g++-9 40

RUN wget https://storage.googleapis.com/golang/go1.7.3.linux-amd64.tar.gz && tar -C /usr/local -xzf go1.7.3.linux-amd64.tar.gz && \
    export PATH=$PATH:/usr/local/go/bin

RUN cd / && mkdir Project && cd Project && mkdir CodeRunner && mkdir Runner && cd Runner && mkdir Code

# RUN cd /Project/Runner && wget -O "CodeRunner" https://hub.fastgit.org/criyle/go-judge/releases/download/v1.3.3/executorserver-amd64 && chmod +x CodeRunner

RUN cd /Project/Runner && wget -O "CodeRunner" https://github.com/criyle/go-judge/releases/download/v1.3.3/executorserver-amd64 && chmod +x CodeRunner

EXPOSE 5000

CMD cd /Project/CodeRunner/ && sh DockerRun.sh
