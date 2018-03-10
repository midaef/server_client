
import threading
import socket
import time


key = 8194

shutdown = False
join = False


def receving (name, sock):
	while not shutdown:
		try:
			while True:
				data, addr = sock.recvfrom(1024)
				decrypt = ""; k = False
				for i in data.decode("utf-8"):
					if i == ":":
						k = True
						decrypt += i
					elif k == False or i == " ":
						decrypt += i
					else:
						decrypt += chr(ord(i)^key)
				print(decrypt)
				time.sleep(0.2)
		except:
			pass


host = socket.gethostbyname(socket.gethostname())
port = 0

server = ("localhost",9090) 

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)
alias = input("Name: ")
s.sendto(("["+ alias + "] <= join server ").encode("utf-8"),server)
s.sendto((alias).encode("utf-8"),server)
rT = threading.Thread(target = receving, args = ("RecvThread",s))
rT.start()
while shutdown == False:
	try:
		s.sendto((input('>>>').lstrip().rstrip()).encode("utf-8"),server)
	except:
		s.sendto(("["+ alias + "] <= left server ").encode("utf-8"),server)
		shutdown = True


rT.join()
s.close()