import contextlib
import socket


@contextlib.contextmanager
def connect(host):
    """
    Connect to EventStore server on default 1113 port.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, 1113))
    try:
        yield sock
    finally:
        sock.close()
