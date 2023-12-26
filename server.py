import socket

host = "127.0.0.1"
port = 1234

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))

s.listen()

(connection,address) = s.accept()

if connection:
    print(f"Bir kullanici baglandi: {address}")
    while 1:

        ldata = connection.recv(1024)

        if ldata.decode("utf-8") == "exit":
            connection.close()

        else:
            print(ldata.decode("utf-8"))


        data = input("Message: ")

        if data.encode("utf-8") == "exit":
            connection.close()

        else:
            connection.sendall(data.encode("utf-8"))
