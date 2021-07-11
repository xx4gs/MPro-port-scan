import socket
import sys as p
import time as mp
def slow(m2):
	for m1 in m2 + '\n':
		p.stdout.write(m1)
		p.stdout.flush()
		mp.sleep(1. / 120)
slow("""
__________________________________
|                                |
|    __________________          |
|   |  Telegram:xx4gs  |         |
|   |  Instagram:xx4gs |         |
|   |__________________|         |
|     ______________________     |
|    |  MohammedPro💉      |     |
|    |  port_scan.py💉     |     |
|    |_____________________|     |
|________________________________|
""")
MPro_site = input('[MPro حط رابط الموقع ] >> ')
MPro_ip  = socket.gethostbyname(MPro_site)
print("\n Website \n\n",MPro_ip)
try:
	host = input("\n [MPro🇸🇦] حط الايبي الي تبي تفحصه >> ")
	for port in range(1,2000):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(0.1)
		result = s.connect_ex((host,port))
		if result == 0:
			print("the port {} yas open.".format(port))
		else:
			print("the port {} no open.".format(port))
except:
    print("Error")
