# coding:UTF-8
# Author:小范同学

import threading
import socket
import struct
import sys
import time


def socket_service():
    try:
        # 连接到本机端监听本机特定的端口号
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('xx.xx.xx.xx', 8080))
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print('Waiting connection...')

    while 1:
        # 接收文件
        conn, addr = s.accept()
        t = threading.Thread(target=deal_data, args=(conn, addr))
        t.start()


# 处理接收的数据
def deal_data(conn, addr):
    print('Accept new connection from {0}'.format(addr))
    conn.send('Hi, Welcome to the server!'.encode('utf-8'))

    while 1:
        fileinfo_size = struct.calcsize('128sl')
        buf = conn.recv(fileinfo_size)
        if buf:
            filename, filesize = struct.unpack('128sl', buf)
            fn = filename.strip(b'\00')
            fn = fn.decode()
            print('file new name is {0}, filesize if {1}'.format(str(fn), filesize))

            recvd_size = 0
            fp = open('./' + str(fn), 'wb')
            print('start receiving...')
            begin = time.time()

            while not recvd_size == filesize:
                if filesize - recvd_size > 1024:
                    data = conn.recv(1024)
                    recvd_size += len(data)
                else:
                    data = conn.recv(filesize - recvd_size)
                    recvd_size = filesize
                fp.write(data)
            fp.close()
            end = time.time()
            print('end receive and cost %f s' % (end - begin))
        conn.close()
        break


if __name__ == "__main__":
    socket_service()
