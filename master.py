import socket
import sys
import RPi.GPIO as GPIO

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

def left():
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(2, GPIO.LOW)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(7, GPIO.LOW)

def back():
    GPIO.output(2, GPIO.HIGH)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(7, GPIO.LOW)

def forward():
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(2, GPIO.LOW)
    GPIO.output(7, GPIO.HIGH)
    GPIO.output(17, GPIO.LOW)


def create_socket():
    try:
        global host
        global s
        global port
        host=""
        port=9999
        s=socket.socket()
    except socket.error as mag:
        print("socket creation error",str(mag))


def bind_socket():
    try:
        global host
        global s
        global port

        print("binding the socket")
        s.bind((host,port))
        s.listen(5)


    except socket.error as mag:
        print("socket binding error ",str(mag)," retrying")
        bind_socket()


def accept():
    conn,adress=s.accept()
    print("ip : ",adress[0]," port : ",adress[1])
    send_command(conn)
    conn.close()


def send_command(conn):
    while True:
        #print("hi")
        cmd=input()
        if(cmd=="quit"):
            conn.close()
            s.close()
            sys.exit()
        if(cmd == 'right'):
            conn.send(str.encode(cmd))
            right()
            #client_response=str(conn.recv(1024),"utf-8")
        elif(cmd == 'left'):
            conn.send(str.encode(cmd))
            left()
            #client_response = str(conn.recv(1024), "utf-8")
        elif(cmd == 'back'):
            conn.send(str.encode(cmd))
            back()
            #client_response = str(conn.recv(1024), "utf-8")
        else:
            conn.send(str.encode(cmd))
            forward()






def main():
    create_socket()
    bind_socket()
    accept()

main()

