def submit_data(data, client, address):
    #import socket
    #client = socket.socket()
    client.connect(address)
    client.send(data.encode())
    client.close()
