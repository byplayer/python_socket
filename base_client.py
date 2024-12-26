import socket


class BaseClient:
    def __init__(self, timeout: int = 10, buffer: int = 1024):
        self.__socket = None
        self.__timeout = timeout
        self.__buffer = buffer

    def connect(self, host, port):
        self.__socket = socket.socket()
        self.__socket.settimeout(self.__timeout)
        print(f"{socket.getaddrinfo(host, port, 0, socket.SOCK_STREAM)}")
        addr = socket.getaddrinfo(host, port, 0, socket.SOCK_STREAM)[-1][-1]
        self.__socket.connect(addr)

    def send(self, message: str = "") -> None:
        flag = False
        while True:
            if message == "":
                message_send = input("> ")
                if message_send == "":
                    continue
                print(f"{message_send=}")
                if message_send == "c":
                    flag = True
            else:
                message_send = message
                # flag = True

            self.__socket.send(message_send.encode('utf-8'))
            message_recv = self.__socket.recv(self.__buffer).decode('utf-8')
            self.received(message_recv)
            if flag:
                break
        try:
            self.__socket.shutdown(socket.SHUT_RDWR)
            self.__socket.close()
        except Exception as ex:
            print(
                f"socket close exception:{type(ex)}:{ex}")

    def received(self, message: str):
        print(message)
        print(len(message))
