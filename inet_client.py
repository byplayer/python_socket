import socket

from base_client import BaseClient


class InetClient(BaseClient):
    def __init__(self, host: str = "127.0.0.1", port: int = 8085) -> None:
        super().__init__(timeout=60, buffer=4096)
        super().connect(host, port)


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
