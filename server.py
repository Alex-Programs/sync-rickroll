import socket
import time
from threading import *

HOST = "0.0.0.0"
PORT = 1085
BUFFERSIZE = 4096


class shared():
    clients = []


def handle_conn(conn, addr):
    print("[+] Connection from: {}".format(addr))
    shared.clients.append(conn)

def start():
    startDelta = 2
    startTime = time.time()
    for client in shared.clients:
        try:
            data = ("DATA:" + str(startDelta - (time.time() - startTime)) + ":END DATA").encode("utf8")
            print(str(data))
            client.send(data)
        except Exception as e:
            print(e)

    while True:
        print(str(startDelta - (time.time() - startTime)))
        time.sleep(0.1)
        if startDelta - (time.time() - startTime) < 0:
            break


def listen_to_start():
    while True:
        input("")
        start()


Thread(target=listen_to_start).start()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    while True:
        try:
            s.bind((HOST, PORT))
            print("Bound at " + str(PORT))
            break
        except:
            PORT += 1

    while True:
        s.listen()

        conn, addr = s.accept()

        Thread(target=handle_conn, args=(conn, addr)).start()
