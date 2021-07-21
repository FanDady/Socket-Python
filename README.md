# Socket-Python

This repository mainly provides the realization of the communication between the client and the cloud server. The main way is to connect TCP through the socket library of Python

# Development Environment
- Python3.7
- socket
- time
- os
- struct
- cv2
- time
- windows/linux

# Content
```
|-- README.md
|-- camera_client.py    # the client of open camera and sending video file
|-- file_client.py      # the client of sending file
|-- file_server.py      # the server of receiving file
|-- text_client.py      # the client of sending text
|-- text_server.py      # the server of receiving text
```

# How to use
- Set the hostname and the port ; set the public IP in the client file and set the private IP in the server file  
![images1](https://github.com/FanDady/blob/Socket-Python/images/1.jpg)  
![images1](https://github.com/FanDady/blob/Socket-Python/images/2.jpg)

- if need to transfer the file , run the server file firstly in the cloud server  
``` python file_server.py```  

- if need to transfer the text , run the server file firstly in the cloud server  
``` python text_server.py```  

- if need to send the file , run the client file then in the client device  
```python file_client.py```  
- if need to open camera and send the file , run the client file then in the client device  
```python camera_client.py```  
- if need to send the text , run the client file then in the client device  
```python text_client.py```
