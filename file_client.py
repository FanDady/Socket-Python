"""
the client of sending any file
"""

import os
import sys
import struct
import socket


def socket_client():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 8080))
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print(s.recv(1024))

    filepath = './filename'

    if os.path.isfile(filepath):
        filein_size = struct.calcsize('128sl')
        ahead = struct.pack('128sq', os.path.basename(filepath).encode('utf-8'), os.stat(filepath).st_size)
        s.send(ahead)
        fp = open(filepath, 'rb')
        while 1:
            data = fp.read(1024)
            if not data:
                print('{0} file send over...'.format(os.path.basename(filepath)))
                break
            s.send(data)
        s.close()


if __name__ == '__main__':
    socket_client()
