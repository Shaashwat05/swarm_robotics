import socket
import os
import subprocess
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)


def right():
    GPIO.output(2, GPIO.HIGH)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(7, GPIO.HIGH)
    GPIO.output(17, GPIO.LOW)
    time.sleep(0.5)


def left():
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(2, GPIO.LOW)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(7, GPIO.LOW)
    time.sleep(0.5)


def back():
    GPIO.output(2, GPIO.HIGH)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(7, GPIO.LOW)
    time.sleep(0.5)


def forward():
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(2, GPIO.LOW)
    GPIO.output(7, GPIO.HIGH)
    GPIO.output(17, GPIO.LOW)
    time.sleep(0.5)


s = socket.socket()
host = "172.16.248.218"
port = 9999

s.connect((host, port))

while (True):
    data = s.recv(1024)
    data = data.decode(("utf-8"))
    if (data == 'right'):
        right()
        # client_response=str(conn.recv(1024),"utf-8")
    elif (data == 'left'):
        left()
        # client_response = str(conn.recv(1024), "utf-8")
    elif (data == 'back'):
        back()
        # client_response = str(conn.recv(1024), "utf-8")
    else:
        forward()
