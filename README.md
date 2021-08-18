# Socket-Python
主要实现客户端即工控机和云服务器端进行的文件传输，使用的主要方法是通过Socket传输，其底层就是TCP连接传输，主要目的是工控机将录制的视频传输到云端储存，其应用背景可为目标检测等；其中云服务器端必须一直运行接收文件的程序，而客户端只需要连接云服务器端的公网进入特定端口号即可实现连接。

# Development Environment
- Python3
- socket
- time
- struct
- cv2
- os

# Content
```
|-- README.md
|-- camera_client.py    # 使用摄像头进行视频录制并传输文件的客户端代码
|-- file_client.py      # 传输任何文件的客户端代码
|-- file_server.py      # 接收任何文件的服务端代码
|-- text_client.py      # 传输文本信息的客户端代码
|-- text_server.py      # 接收文本信息的服务端代码
|-- server.py           # 集成MQTT和Socket的服务端代码

# 其中传输和接收文本信息的代码有点冗余了但是还是都放上去，真正主要的代码并可移植
# 的就是file_client和file_server，camera_client主要是测试在目标检测的时候客户
# 端模拟检测到目标并录制一小段视频然后录制完毕就马上传输到云服务器
```

# How to use
- 开通云服务器，并且打开特定端口，端口可以自己指定没有特别要求，但是有些端口号默认是被占用的
- 在客户端代码中设置好要连接的公网IP和指定的端口号，然后运行```python file_client.py```  
![images1](https://z3.ax1x.com/2021/08/18/foxLz4.png)

- 在云服务器上同样设置好端口号及云服务器的本地IP，然后运行```python file_server.py```


# Results
- 下面展示了云服务器端接收和客户端模拟发送视频文件的结果图  
  
![images3](https://z3.ax1x.com/2021/08/18/fordTU.jpg)  

![images4](https://z3.ax1x.com/2021/08/18/forsp9.jpg)  
  
 <div align="center">
    <a href="mailto:Yuri.Fanzhiwei@gmail.com">
        <img src="https://z3.ax1x.com/2021/08/17/f47afP.png" width="3%"/>
    </a>
    <img width="3%" />
    <a href="https://github.com/FanDady">
        <img src="https://z3.ax1x.com/2021/08/17/f45ZCT.png" width="3%"/>
    </a>
    <img width="3%" />
    <a href="https://twitter.com/ZhiweiFan6">
        <img src="https://z3.ax1x.com/2021/08/17/f45rIP.png" width="3%"/>
    </a>
    <img width="3%" />
    <a href="https://www.youtube.com/channel/UCGa3AFKcZCt8btPnHVuKzRw">
        <img src="https://z3.ax1x.com/2021/08/17/f4Ibkt.png" width="3%"/>
    </a>
    <img width="3%" />
    <a href="https://www.facebook.com/profile.php?id=100071474933884">
        <img src="https://z3.ax1x.com/2021/08/17/f4oSmj.png" width="3%"/>
    </a>
    <img width="3%" />
    <a href="https://weibo.com/u/5869896682/home">
        <img src="https://z3.ax1x.com/2021/08/17/f4o97n.png" width="3%"/>
    </a>
    <img width="3%" />
    <a href="https://www.zhihu.com/people/fan-zhi-wei-68">
        <img src="https://z3.ax1x.com/2021/08/17/f4oE1U.png" width="3%"/>
    </a>
    <img width="3%" />
    <a href="https://blog.csdn.net/qq_43711697?spm=1000.2115.3001.5343">
        <img src="https://z3.ax1x.com/2021/08/17/f47j1K.png" width="3%"/>
    </a>
</div>
