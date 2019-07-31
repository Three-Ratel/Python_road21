# docker部署

## 1. pull环境

```nginx
docker pull centos
docker pull nginx
```

- 测试启动

```nginx
docker  run -ti --rm  centos:latest  bash
docker run -ti --rm -p 81:80 nginx bash
```

## 2. yum配置

- **EPEL** (Extra Packages for Enterprise Linux)

```nginx
yum -y install epel-release
yum -y insatll vim
yum -y install python36
```

# Part1 Orientation

## 1. Test Docker version

```nginx
# 查看当前docker版本号
~ docker --version / -v
# 输出
Docker version 18.09.2, build 6247962
```

- Run `docker info` (or `docker version` without `--`) to view even more details about your Docker installation
- docker version：信息较少

```nginx
~ docker info

Containers: 2
 Running: 1
 Paused: 0
 Stopped: 1
Images: 3
Server Version: 18.09.2
Storage Driver: overlay2
 Backing Filesystem: extfs
...
```

## 2. Recap and cheat sheet

```nginx
# 查看本机所有镜像
docker image ls
docker images
# List Docker containers (running, all, all in quiet mode)
docker container ls
docker container ls --all
docker container ls -aq
```

# Part2 Containers

## 1. 进入容器

```nginx
docker ps
docker exec -it d1fe90d74edc /bin/bash
sudo docker attach 容器ID  
```

- 删除镜像先删除container

```nginx
# 删除一个image
docker rmi <image id>
# 删除所有image
docker rmi $(docker images -q)
```

## 2. 把容器打包成镜像

```nginx
docker commit 容器id centos-vim
```

## 3. Dockerfile

### 3.1 创建dockerfile文件

```nginx
# Use an official Python runtime as a parent image
FROM python:2.7-slim
# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app
# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
# Make port 80 available to the world outside this container
EXPOSE 80
# Define environment variable
ENV NAME World
# Run app.py when the container launches
CMD ["python", "app.py"]
```

### 3.2 创建app和requirements.txt

#### 1. requirements.txt

```nginx
Flask
Redis
```

#### 2. app.py

```nginx
from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)
app = Flask(__name__)
@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
```

#### 3. build app

- Here's what ls should show

```nginx
$ ls
Dokerfile	 app.py 	requirements.txt
```

- 创建镜像，存储到本机Docker image registry

```nginx
docker build --tag/-t=friendlyhello .
# 查看镜像
$ docker images
```

- tag默认是`latest`,完整语法

```nginx
--tag=friendlyhello:v0.0.1
```

#### Note for Linux

- Linux 用户proxy server settings
- ENV command 指定host 和 port

```nginx
# set proxy server, replace host:port with values for your servers
ENV http_proxy host:port
ENV http_proxy host:port
```

- DNS settings:DNS设置不当`pip`不能正常使用，需要设置DNS server使 pip 正常使用，为Docker daemon设置DNS编辑 `/etc/docker/daemon.json` 

```nginx
{
  	'dns':['your_dns_address', '8.8.8.8']
}
```

- 本机的dns不可用时，使用goole的dns，保存后重启docker service

```nginx
sudo service docker restart
```

#### 4. Run the app

- 运行app，mapping 主机port 4000 端口和 80 使用 `-p`

```nginx
docker run -p 4000:80 friendlyhello
```

- 使用`http://0.0.0.0:80`查看或`curl http://localhost:4000`
- 后台运行app

```nginx
docker run -d -p 4000:80 friendlyhello
```

#### 5. Log in with your Docker ID

```nginx
docker login
# 或者
docker login -u 用户名 -p 密码
```

- 推送image到Docker Hub

```nginx
# 添加tag标dock
docker tag image username/repository:tag
# For example
docker tag friendlyhello henrywzh/get-started:part2
```

- Publish the image

```nginx
docker push henry/repository:tag
```

- 先在其他终端上登录：再运行app

```nginx
docker run -p 4000:80 hernywzh/test:friendlyhello
```

# Part3 Services

## 1. docker-compose.yml

- 定义docker容器的参数

```nginx
version: "3"
services:
  web:
    # replace username/repo:tag with your name and image details
    image: henrywzh/test:hello
    deploy:
      replicas: 5
      resources:
        limits:
          cpus: "0.1"
          memory: 50M
      restart_policy:
        condition: on-failure
    ports:
      - "4000:80"
    networks:
      - webnet
networks:
  webnet:
```

## 2. Run new load-balanced app

### 1. `docker stack deploy`命令

- 需要执行如下命令

```nginx
docker swarm init
```

### 2. 为app命名

- A single container running in a service is called a **task**
- web服务的名称为 **app名称_web**

```nginx
docker stack deploy -c docker-compose.yml app名称(如：mytest)
# 获取service ID
docker service ls
# 查看所有服务with stack
docker stack services mytest
# 展示服务的所有task
docker service ps mytest_web
# 展示所有容器的id
docker container ls -q
```

### 3. Scale the app

```nginx
# 修改docker-compose.yml中的replicas=3参数
# 重新部署即可
docker stack deploy -c docker-compose.yml mytest_web
docker stack service ps mytest_web
# 显示如下
ID                  NAME                IMAGE                 NODE                    DESIRED STATE       CURRENT STATE            ERROR               PORTS
o8fq9vr1lt04        mytest_web.1        henrywzh/test:hello   linuxkit-025000000001   Running             Running 11 minutes ago                       
z5cyi8z0xrje        mytest_web.2        henrywzh/test:hello   linuxkit-025000000001   Running             Running 11 minutes ago                       
cjsancy3bgpv        mytest_web.3        henrywzh/test:hello   linuxkit-025000000001   Running             Running 11 minutes ago                       
k1ogibpmrnn2        mytest_web.4        henrywzh/test:hello   linuxkit-025000000001   Remove              Running 14 seconds ago                       
sgddt44fe5aw        mytest_web.5        henrywzh/test:hello   linuxkit-025000000001   Remove              Running 14 seconds ago                       
```

### 4. take down the app and the swarm 

#### 1. Take the app down

```nginx
docker stack rm mytest_web
```

#### 2. Take down the swarm

```nginx
docker swarm leave --force
```

# Part4 Swarms

## 1. swarms definaiton

- We've deployed an application onto a cluster, running it on multiple machines. **Multi-container, multi-machine** applications are made possible by joining **multiple machines** into a “Dockerized” cluster called a **swarm**.

## 2. Understanding Swarm clusters













