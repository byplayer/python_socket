import socket
import sys
import traceback


class BaseClient:
    def __init__(self, timeout: int = 10, buffer: int = 1024):
        self.__socket = None
        self.__address = None
        self.__timeout = timeout
        self.__buffer = buffer

    def connect(self, address, family: int, typ: int, proto: int):
        self.__address = address
        self.__socket = socket.socket(family, typ, proto)
        self.__socket.settimeout(self.__timeout)
        self.__socket.connect(self.__address)

    def send(self, message: str = "") -> None:
        flag = False
        while True:
            if message == "":
                message_send = input("> ")
                if message_send == "quit":
                    flag = True
            else:
                message_send = message
                flag = True

            self.__socket.send(message_send.encode('utf-8'))
            message_recv = self.__socket.recv(self.__buffer).decode('utf-8')
            self.received(message_recv)
            if flag:
                break
        try:
            self.__socket.shutdown(socket.SHUT_RDWR)
            self.__socket.close()
        except:
            etype, value, tb = sys.exc_info()
            print(
                "socket close exception:" +
                "\n".join(traceback.format_exception(etype, value, tb)))

    def received(self, message: str):
        print(message)
