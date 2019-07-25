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
```

- 删除镜像先删除container

```nginx
# 删除一个image
docker rmi <image id>
# 删除所有image
docker rmi $(docker images -q)
```



