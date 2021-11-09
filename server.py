import socket
import time
from threading import *
import argparse

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
            data = ("START:" + str(startDelta - (time.time() - startTime))).encode("utf8")
            print(str(data))
            client.send(data)
        except Exception as e:
            print(e)

    while True:
        print(str(startDelta - (time.time() - startTime)))
        time.sleep(0.1)
        if startDelta - (time.time() - startTime) < 0:
            break


def kill():
    for client in shared.clients:
        try:
            data = ("KILL:JUST DIE").encode("utf8")
            print(str(data))
            client.send(data)
        except Exception as e:
            print(e)


def listen_to_start():
    while True:
        data = input("")
        if data == "start":
            start()

        elif data == "kill":
            kill()

def main():
    parser = argparse.ArgumentParser(description="Synchronised rickrolls!")

    parser.add_argument("host", type=str, default="0.0.0.0", help="Host")
    parser.add_argument("port", type=int, default=1085, help="Port")

    args = vars(parser.parse_args())

    HOST = args["host"]
    PORT = args["port"]

    BUFFERSIZE = 4096

    args = vars(parser.parse_args())

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

main()