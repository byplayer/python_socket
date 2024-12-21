import socket
import sys
import traceback

from base_client import BaseClient


class InetClient(BaseClient):
    def __init__(self, host: str = "127.0.0.1", port: int = 8085) -> None:
        self.server = (host, port)
        super().__init__(timeout=60, buffer=4096)
        super().connect(self.server, socket.AF_INET, socket.SOCK_STREAM, 0)


if __name__ == "__main__":

    while True:
        try:
            cli = InetClient()
            cli.send()
        except Exception:
            etype, value, tb = sys.exc_info()
            print(
                "socket close exception:" +
                "\n".join(traceback.format_exception(etype, value, tb)))

    # for i in range(200):
    #     cli.send("r")
