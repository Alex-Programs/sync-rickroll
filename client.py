import socket
import time
import simpleaudio as sa
import simpleaudio.functionchecks as fc

#fc.LeftRightCheck.run()

HOST = input("Host: ")
PORT = int(input("Port: "))

BUFFERSIZE = 4096

soundobjs = []

obj = sa.WaveObject.from_wave_file("starman.wav")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        while True:
            signal, data = s.recv(BUFFERSIZE).decode("utf8").split(":")

            if signal == "START":
                break
            elif signal == "KILL":
                for obj in soundobjs:
                    obj.stop()
            else:
                print(signal, data)

        print("Start in " + str(data))

        time.sleep(float(data))

        print("Starting")
        soundobjs.append(obj.play())