import socket
import time
import simpleaudio as sa
import simpleaudio.functionchecks as fc

#fc.LeftRightCheck.run()

HOST = input("Host: ")
PORT = int(input("Port: "))

BUFFERSIZE = 4096

obj = sa.WaveObject.from_wave_file("starman.wav")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        resp = s.recv(BUFFERSIZE).decode("utf8").split(":")[1]

        if resp:
            break

    print("Start in " + str(resp))

    time.sleep(float(resp))

    obj = obj.play()
    obj.wait_done()