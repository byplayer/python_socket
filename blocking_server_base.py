import socket
import sys
import traceback


class BlockingServerBase:
    def __init__(self, timeout: int = 60 * 60 * 60, buffer: int = 1024):
        self.__socket = None
        self.__timeout = timeout
        self.__buffer = buffer
        self.close()

    def __del__(self):
        self.close()

    def close(self) -> None:
        if self.__socket is None:
            return

        try:
            self.__socket.shutdown(socket.SHUT_RDWR)
        except Exception:
            etype, value, tb = sys.exc_info()
            print(
                "shutdown error:" +
                "\n".join(traceback.format_exception(etype, value, tb)))

        try:
            self.__socket.close()
        except Exception:
            etype, value, tb = sys.exc_info()
            print(
                "shutdown error:" +
                "\n".join(traceback.format_exception(etype, value, tb)))
        finally:
            self.__socket = None

    def accept(self, address, family: int, typ: int, proto: int) -> None:
        self.__socket = socket.socket(family, typ, proto)
        self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__socket.settimeout(self.__timeout)
        self.__socket.bind(address)
        self.__socket.listen(1)
        print("Server started :", address)
        conn, _ = self.__socket.accept()

        while True:
            try:
                message_recv = conn.recv(self.__buffer).decode('utf-8')
                message_resp = self.respond(message_recv)
                conn.send(message_resp.encode('utf-8'))
                if (message_recv == "quit"):
                    break
            except ConnectionResetError:
                etype, value, tb = sys.exc_info()
                print(
                    "connection reset error:" +
                    "\n".join(traceback.format_exception(etype, value, tb)))
                break
            except BrokenPipeError:
                etype, value, tb = sys.exc_info()
                print(
                    "broken pipe error:" +
                    "\n".join(traceback.format_exception(etype, value, tb)))
                break
        self.close()

    def respond(self, message: str) -> str:
        return ""
