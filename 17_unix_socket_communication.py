"""
System Calls: socketpair(2), recv(2), send(2)
"""
import os 
import socket
# 同じマシン上の通信なのでソケットファミリーはAF_UNIX
child_socket, parent_socket = socket.socketpair(socket.AF_UNIX, socket.SOCK_DGRAM, 0)
# MAXバッファサイズを1000
maxlen = 1000

if __name__ == "__main__":
    pid = os.fork() 
    if pid == 0:
        parent_socket.close()

        for i in range(4):
            instruction = child_socket.recv(maxlen)
            child_socket.send(b"%s accomplished!" % instruction)
    else:
        child_socket.close()

        for i in range(2):
            parent_socket.send(b"Heavy lifting", 0)

        for i in range(2):
            parent_socket.send(b"Feather lifting", 0)

        for i in range(4):
            print(parent_socket.recv(maxlen))
