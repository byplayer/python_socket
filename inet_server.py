import socket

from blocking_server_base import BlockingServerBase


class InetServer(BlockingServerBase):
    def __init__(self, host: str = "0.0.0.0", port: int = 8099) -> None:
        self.server = (host, port)
        super().__init__(timeout=60*60*60, buffer=1024)
        self.accept(self.server, socket.AF_INET, socket.SOCK_STREAM, 0)

    def respond(self, message: str) -> str:
        print("received -> ", message)
        return f"Server accepted !!({message})"


if __name__ == "__main__":
    InetServer()
