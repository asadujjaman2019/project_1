import socket
port=12345
host = "127.0.0.1"

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket successfully created")

s.bind((host,port))
print("socket bind to>>" ,port)

s.listen(5)
print("socket is listining")

while True:

    c,addr=s.accept()
    print("got connection from my pc",addr)

    c.send("thank u for connecting shiplu".encode())

    c.close()
    break
