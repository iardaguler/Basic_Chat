import socket

host = "127.0.0.1"
port = 1234

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((host,port))

while 1:

    data = input("Message: ")

    if data.encode("utf-8") == "exit":
        print("Bir kullanici ayrildi")

    else:
        s.sendall(data.encode("utf-8"))


    ldata = s.recv(1024)

    if ldata.decode("utf-8") == "exit":
        print(f"Bir kullanici ayrildi {s}")

    else:
        print(ldata.decode("utf-8"))


