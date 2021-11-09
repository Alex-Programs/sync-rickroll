import socket
import time
import simpleaudio as sa
import simpleaudio.functionchecks as fc
import argparse

def main():
    parser = argparse.ArgumentParser(description="Synchronised rickrolls!")
    parser.add_argument("host", type=str, default="127.0.0.1", help="Hostname")
    parser.add_argument("port", type=int, default=1085, help="Port")


    args = vars(parser.parse_args())

    #fc.LeftRightCheck.run()

    HOST = args["host"]
    PORT = args["port"]

    BUFFERSIZE = 4096

    soundobjs = []

    obj = sa.WaveObject.from_wave_file("rickroll.wav")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("Connected")
        while True:
            while True:
                print("Waiting for data")
                signal, data = s.recv(BUFFERSIZE).decode("utf8").split(":")

                if signal == "START":
                    print("Received start signal")
                    break
                elif signal == "KILL":
                    print("Received kill signal")
                    for obj in soundobjs:
                        obj.stop()
                else:
                    print(signal, data)

            print("Start in " + str(data))

            time.sleep(float(data))

            print("Starting")
            soundobjs.append(obj.play())

main()