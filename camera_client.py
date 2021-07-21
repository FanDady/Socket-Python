"""
open the camera and record ,then save the video and send the file to the cloud server
"""

import os
import sys
import cv2
import socket
import struct

if __name__ == "__main__":
    # set the camera device
    cap = cv2.VideoCapture(1)

    # set the display window and size
    cv2.namedWindow('CAP', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("CAP", cv2.WND_PROP_FULLSCREEN, cv2.WND_PROP_FULLSCREEN)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    # set the encoding format
    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')

    # set the video's filename and output FPS
    out = cv2.VideoWriter('output.avi', fourcc, 30, (1920, 1080))
    while True:
        ret, frame = cap.read()
        out.write(frame)
        cv2.imshow('CAP', frame)
        esc = cv2.waitKey(1)
        # enter the key 'q' to quit recording
        if esc == ord('q'):
            break
    cap.release()
    out.release()
    cv2.destroyWindow('CAP')

    # client connect to the cloud server
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # set the cloud server's public IP and open port
        s.connect(('47.104.88.125', 8080))

    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print(s.recv(1024))

    # set the file path
    filepath = './output.avi'

    if os.path.isfile(filepath):
        # get the filename and encode with 'UTF-8'
        file_size = struct.calcsize('128sl')
        head = struct.pack('128sq', os.path.basename(filepath).encode('utf-8'), os.stat(filepath).st_size)
        s.send(head)
        fp = open(filepath, 'rb')

        # send the file
        while 1:
            data = fp.read(1024)
            if not data:
                print('{0} file send over...'.format(os.path.basename(filepath)))
                break
            s.send(data)
        s.close()

    print('finished')
