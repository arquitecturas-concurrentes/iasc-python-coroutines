def fetch(url):
    sock = socket.socket()
    sock.connect(('bla.com', 80))
    request = 'GET {} HTTP/1.0\r\nHost: bla.com\r\n\r\n'.format(url)
    sock.send(request.encode('ascii'))
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        chunk = sock.recv(4096)

    parse_response(response)