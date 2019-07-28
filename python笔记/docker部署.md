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

```nginx
$ ls
Dokerfile	 app.py 	requirements.txt
```

- 创建镜像，存储到本机Docker image registry

```nginx
docker build --tag/-t=friendlyheloo
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
```

- 推送image到Docker Hub

```nginx
docker tag image username/repository:tag
# For example
docker tag friendlyhello henry/get-started:part2
```

- Publish the image

```nginx
docker push henry/repository:tag
```

- 再其他终端上运行app

```nginx
docker run -p 4000:80 username/repository:tag
```















