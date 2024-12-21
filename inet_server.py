import os
import socket
import sys

from blocking_server_base import BlockingServerBase


class InetServer(BlockingServerBase):
    def __init__(self, host: str = "0.0.0.0", port: int = 8085) -> None:
        self.server = (host, port)
        super().__init__(timeout=60*60*60, buffer=1024)
        while True:
            self.accept(self.server, socket.AF_INET, socket.SOCK_STREAM, 0)

    def respond(self, message: str) -> str:
        print("received -> ", message)
        return f"Server accepted !!({message})"


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "-d":
        print("daemon")
        pid_dir = os.path.join(os.path.dirname(__file__), "tmp")
        os.makedirs(pid_dir, exist_ok=True)
        pid_base = os.path.splitext(os.path.basename(__file__))[0]
        pid_path = os.path.join(pid_dir, f"{pid_base}.pid")
        pid = os.fork()
        if pid > 0:
            f = open(pid_path, 'w')
            f.write(str(pid)+"\n")
            f.close()
            sys.exit()
        else:
            InetServer()
    else:
        InetServer()
