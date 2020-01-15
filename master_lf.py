import socket
import sys
import RPi.GPIO as GPIO



GPIO.setmode(GPIO.BOARD)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(5, GPIO.IN)
GPIO.setup(6, GPIO.IN)



def right():
    GPIO.output(2, GPIO.HIGH)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(7, GPIO.HIGH)
    GPIO.output(17, GPIO.LOW)
    #time.sleep(0.5)

def left():
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(2, GPIO.LOW)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(7, GPIO.LOW)
    #time.sleep(0.5)

def back():
    GPIO.output(2, GPIO.HIGH)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(7, GPIO.LOW)
    #time.sleep(0.5)

def forward():
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(2, GPIO.LOW)
    GPIO.output(7, GPIO.HIGH)
    GPIO.output(17, GPIO.LOW)
    #time.sleep(0.5)


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
        if (GPIO.input(5) == True and GPIO.input(6) == False):
            conn.send(str.encode("left"))
            left()
        elif(GPIO.input(5) == False and GPIO.input(6) == True):
            conn.send(str.encode("right"))
            right()
        elif (GPIO.input(5) == True and GPIO.input(6) == True):
            conn.send(str.encode("forward"))
            forward()
        elif (GPIO.input(5) == False and GPIO.input(6) == False):
            conn.send(str.encode("back"))
            back()
            break






def main():
    create_socket()
    bind_socket()
    accept()

main()
