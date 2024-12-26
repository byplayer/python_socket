import socket

from base_client import BaseClient

HOST = "roboberry.local"
# HOST = "192.168.11.123"
PORT = 8085


class InetClient(BaseClient):
    def __init__(self, host: str = HOST, port: int = PORT) -> None:
        super().__init__(timeout=60, buffer=4096)
        self.connect(host, port)


if __name__ == "__main__":
    cli = InetClient()
    cli.send()

    # while True:
    #     try:
    #         cli = InetClient()
    #         cli.send()
    #     except Exception as ex:
    #         print(
    #             f"socket close exception:{type(ex)}:{ex}")

    # for i in range(200):
    #     cli.send("r")
