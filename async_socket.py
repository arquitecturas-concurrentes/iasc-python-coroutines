sock = socket.socket()
try:
    sock.connect(('bla.com', 80))
except BlockingIOError:
    pass

# ==================================

from selectors import DefaultSelector, EVENT_WRITE

selector = DefaultSelector()

sock = socket.socket()
sock.setblocking(False)
sock.connect(('bla.com', 80))

def connected():
    selector.unregister(sock.fileno())
    print('connected!')

selector.register(sock.fileno(), EVENT_WRITE, connected)

def loop():
    while True:
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback()

loop()
