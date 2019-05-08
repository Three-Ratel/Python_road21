## 今日内容

- 三次握手把回复和请求连接信息合并为一帧，四次挥手由于一方断开连接之后，可能另一方还有数据需要传输，所有不能合并。
- 网络传输的信息用**json** 传递
- 服务端进行**摘要**
- hashlib，加盐的时候可以使用**用户名**
- os.path.isabs()，os.path.basename()
- TCP合包机制和拆包机制：TCP无边界、流式传输
  - 1200bytes 左右

## 1. struct模块

```python
# 把数据转换为四个字节
import struct
struct.pack('i', 1000)   # i 表示整型，l
struct.pack('i', 10)
struct.pack('i', 12)
struct.pack('i', 18)
struct.unpack(i)
```



