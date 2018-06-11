import socket
import time
import random
import struct

class Recev():

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def listen(self):
        self.s.bind((self.ip, self.port))
        filedata = ''
        while True:
            data, addr = self.s.recvfrom(1024)
            # print struct.unpack('II9s3sII256sI',data)[6]
            if struct.unpack('II9s3sII256sI',data)[0]==1:
                filedata = filedata + struct.unpack('II9s3sII256sI',data)[6]
                print struct.unpack('II9s3sII256sI',data)
                # filedata.append(struct.unpack('II9s3sII256sI',data)[6])
                # print len(filedata)
                # print str(struct.unpack('II9s3sII256sI',data)[1])
                fp = open('save'+str(struct.unpack('II9s3sII256sI',data)[1])+'.png','wb')
                fp.write(filedata)
                fp.close()
            else:
                print struct.unpack('II9s3sII256sI',data)

            print '_______________________'
            

            # if struct.unpack('II9s3sII256sI',data)[1] == 5:
            #     # fp = open('save'+str(struct.unpack('II9s3sII256sI',data)[1])+'.png','wb')
            #     # fp.write(filedata)
            #     pass
            # else:
                

if __name__ == '__main__':
    r = Recev('localhost', 8080)
    r.listen()