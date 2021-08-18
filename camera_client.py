# coding:UTF-8
# Author:小范同学

import os
import sys
import cv2
import socket
import struct

if __name__ == "__main__":
    # 设置摄像头设备
    cap = cv2.VideoCapture(0)

    # 设置摄像头显示的分辨率
    cv2.namedWindow('CAP', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("CAP", cv2.WND_PROP_FULLSCREEN, cv2.WND_PROP_FULLSCREEN)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    # 设置录制视频的编码格式
    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')

    # 设置录制视频的文件名以及帧率
    out = cv2.VideoWriter('output.avi', fourcc, 30, (1920, 1080))
    while True:
        ret, frame = cap.read()
        out.write(frame)
        cv2.imshow('CAP', frame)
        esc = cv2.waitKey(1)
        if esc == ord('q'):
            break
    cap.release()
    out.release()
    cv2.destroyWindow('CAP')

    # 客户端开始尝试连接云服务器端
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置要连接的云服务器端的公网IP和端口号
        s.connect(('47.104.88.125', 8080))

    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print(s.recv(1024))

    # 设置要传输视频文件的文件名
    filepath = './output.avi'

    if os.path.isfile(filepath):
        # 获取文件名并用UTF-8编码
        file_size = struct.calcsize('128sl')
        head = struct.pack('128sq', os.path.basename(filepath).encode('utf-8'), os.stat(filepath).st_size)
        s.send(head)
        fp = open(filepath, 'rb')
        # 文件会被拆分成批次进行发送
        # 进入循环发送文件直到文件发送完毕
        while 1:
            data = fp.read(1024)
            if not data:
                print('{0} file send over...'.format(os.path.basename(filepath)))
                break
            s.send(data)
        s.close()

    print('finished')
