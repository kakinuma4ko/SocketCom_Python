import socket
import time
import random
import struct

class Send():

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.id = '161310110'
        self.name = 'stx'
    
    def send(self, flag, num, pos, size, data, sum):
        # self.s.sendto(msg, (self.ip, self.port))
        sub = struct.pack('II9s3sII256sI',flag,num,self.id,self.name,pos,size,data,sum)
        # print 11
        self.s.sendto(sub, (self.ip, self.port))

        # print len(struct.unpack('II9s3sII256sI',fhead)[6])
        # fp = open('save.data','wb')
        # fp.write(struct.unpack('II9s3sII256sI',sub)[6][0:3])

    def sendfile(self, path):
        fp = open(path, 'rb')
        # s.send(1,0,0,0,fp.read(1024),0)
        filedata = fp.read()
        print filedata
        num = len(filedata)/256
        # print len(filedata),num
        # print len(filedata[0:255])
        s.send(0,num+1,0,0,'',0)
        for i in range(num):
            print i
            s.send(1,i,256*i,256,filedata[256*i:256*(i+1)],0)
            # print filedata[256*(i-1):256*(i)]
        # s.send()
        if len(filedata) % 256 == 0:
            pass
        else:
            s.send(1,num,256*num,len(filedata)%256,filedata[256*num:256*num+1+(num % 256)],0)
            # print filedata[256*num:256*num+1+(num % 256)]
            print len(filedata)%256

if __name__ == '__main__':
    s = Send('localhost',8080)
    s.sendfile('send.png')
