

# docke准备

## 1. 安装docker

```nginx
# 删除旧版本的docker
yum remove docker
# 指定docker-ce源
wget -O /etc/yum.repos.d/docker-ce.repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
# 安装
yum install -y docker-ce
```

```nginx
# 启动docker
systemctl start docker
# 编辑配置文件 /etc/docker/daemon.json
{
    "registry-mirrors": [
        "https://1nj0zren.mirror.aliyuncs.com",
        "https://docker.mirrors.ustc.edu.cn",
        "http://f1361db2.m.daocloud.io",
        "https://registry.docker-cn.com"
    ]
}
# 测试hello-world
docker run -it hello-world
```

## 2. 制作镜像

-   一般使用 乌班图 (较小)
-   作为基础镜像

### 1. dockerfile文件

-   如果复制目录则需要在后面加上目录名称，只复制目录中的文件

```nginx
# 创建dockerfile文件
vim DockerFile
1. 指定基础镜像
FROM 镜像名
2. 构建执行的命令
RUN yum install -y wget
RUN mkdir /mydata
3. 添加文件到 /mydata，如果是压缩包则自动解压
ADD etc.tar.gz /mydata
4. 本地文件copy到镜像中
COPY test.txt /mydata

5. 工作目录，启动后的目(默认根目录)
WORKDIR /mydata
6.ENV设置变量
ENV name=henry
7. VOLUME，指定当前的数据卷
VOLUME ["/data"]
8. EXPOSE,指定 image 的端口，必须声明
EXPOSE 5900
9. LABEL指定标签

10. 执行的命令，只执行最后一个CMD
CMD echo $HOME >> home.txt
CMD ['nginx', 'g', 'daemon off;']
```

```nginx
# 在当前目录下构建
docker build  -t myimage -f 文件名 .
```

```nginx
# 执行，通过浏览器访问测试
docker run -it -P myimage
```

### 2. docker仓库

-   这将使用官方的 registry 镜像来启动私有仓库。
-   默认情况下，仓库会被创建在容器的 /var/lib/registry 目录下。
-   可以通过 -v 参数来将镜像文件存放在本地的指定路径。

```nginx
# 搭建私有 docker 仓库
docker run -d -p 5000:5000 --restart=always -v /opt/register:/var/lib/registery registery

# 修改名称
docker tag redis 127.0.0.1:5000/redis
# push，修改 /etc/docker/daemon.jsonre
{	
	# 本地仓库地址
    "insecure-registries":[
   		"192.168.12.4:5000"
   	]
}

docker push 127.0.0.1:5000/redis
docker push 192.168.12.4:5000/redis
# 其他主机进行 pull redis，也需要修改 /etc/docker/daemon.json
docker push 192.168.12.4:5000/redis
# 查看
curl 127.0.0.1:5000/v2/_catalog
```

### 3. docker-compose

-   docker编排工具：swarms，docker-compose
-   yml/yaml 语法

```nginx
# 安装docker-compose
pip install docker-compose
# yml可以用来做配置文件，后缀名：yml，yaml，数据类型string，int，list，dict...
vim docker-compose.yml
version: "3"			# 和docker版本相对应
services:
	web: 
		build: 
			context: .  					# 指定dockerfile文件目录
			dockerfile: "dockerfile文件"	   # 指定dockerfile文件名
		ports:
		- "3000:5000
	redis:
		image: "redis"	# 镜像名称
:wq
# 启动
docker-compose up
```

```python
# flask应用
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

if __name__ = '__main__':
    app.run('0.0.0.0', 5000)
```

-   yml文件语法

```nginx
# dict类型，冒号、- 后面都必须有空格, 严格要求缩进
name: 'henry'
age: 19
addr:
- 'haidian'
- 'beijing'
```

### 4. 常用命令

```nginx
# 删除 stoped 的容器
docker-compose rm
# 重新构建容器，自动调用当前目录 .yml文件
docker-compose build 
# 查看容器状态
docker-compose ps
# 查看 镜像
docker-compose images
```

# docker部署

## 1. pull环境

```nginx
docker pull centos:tag-name
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
# 查看镜像信息
docker inspect 镜像名
```

## 2. Recap and cheat sheet

### 1. 查看命令

```nginx
# 查看本机所有镜像
docker image ls
docker images
# 只显示 images 的 id
docker images -q
# List Docker containers (running, all, all in quiet mode)
docker container ls
docker container ls --all
docker container ls -aq
# offical 表示是否是docker的官方镜像
docker search mysql

# 查看容器启动后的logs
options：
	-f：实时查看日志
docker logs 容器ID

# 查看容器的资源占用率
docker stats 容器id
# 实时查看日志
docker logs -f 容器id/name
```

### 2. 删除

```nginx
# 删除镜像，只要 run 过就需要先删除 对应的容器,如果tag为none则是其他镜像的依赖
docker rmi 镜像id
# 强制删除image
docker rmi -f 镜像id
# 删除容器
options：
	-f：强制删除
docker rm 容器id/别名
docker rm -f 容器id/别名
# 删除所有 stopped 的容器
docker container prune
# 删除所有容器和镜像
docker rm -f `docker ps -qa`
docker rmi -f `docker images -q`
```

### 3. 启动

```nginx
# 启动容器
格式：docker run [选项] 镜像 [执行的命令]
	-d：表示后台启动，如果启动失败则需要与-it连用
	-it： 交互式终端
	--name：指定启动后的容器名称
	--rm：用于测试使用，退出容器后自动删除
	-v：宿主机目录:容器使用的目录，把容器目录挂载到宿主机
	-p：宿主机port:容器使用的port，把容器使用的port映射到宿主机的port
	-P：宿主机的port是随机的
	
docker run -it redis
```

### 4.备份

```nginx
	 
# 导出镜像
docker save -o redis.tar.gz redis
docker save redis > redis.tar.gz
# 导入镜像
docker load -i redis.tar.gz
docker load < redis.tar.gz
# push镜像
docker commit 容器id			# 生成镜像	
docker tag 镜像id mycentos	# 给镜像加上tag，没有tag则添加，有怎复制一份
docker push repositoryname:tagname
```



# Part2 Containers

## 1. 进入容器

```nginx
docker ps -a
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













