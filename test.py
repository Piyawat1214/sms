from threading import Thread
import random

try:
	import requests
	import os
	import threading
	import time

except ModuleNotFoundError:
	print("\033[91m[!] install requests dulu gan")
	print("\033[95m$ pip install reqests")
	exit()

class warna:
    p = '\033[95m'
    b = '\033[94m'
    g = '\033[92m'
    y = '\033[93m'
    r = '\033[91m'

try:
	os.system('clear')
	print("""\33[1;92m

███████╗██╗░░██╗██╗░░██╗██╗░░██╗ ███████░░░██╗░░██╗
██╔════╝██║░░██║██║░░██║██║░░██║██╔═████╗░ ██║░░██║ 
█████╗░░███████║███████║███████║██║██╔██║░ ███████║ 
██╔══╝░░██╔══██║╚════██║╚════██║████╔╝██║░ ╚════██║
███████╗██║░░██║░░░░░██║░░░░░██║███████╔╝░░░░░░ ██║
╚══════╝╚═╝░░╚═╝░░░░░╚═╝░░░░░╚═╝╚═════╝░░░░░░░░ ╚═╝   
         
""")
	print ("")
	print ("CREDIT : EH4404")
	print ("ทำโดย : สมชาย สบายดี")
	print ("")
	phone = input("\033[95m[×] เบอร์ : \033[0m")
	num=int(input("\033[95m[×] จำนวน : \033[0m"))

except ValueError:

	print ("\033[91m[!] ใส่ไม่ถูกต้อง")
	exit()
print('')
print("-------------------- Start -----------------------")
print('')

name = ''
for x in range(12):
        name = name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))


	

for i in range(num):
    time.sleep(1)
    threading.Thread(target=API_1).start()
    threading.Thread(target=API_2).start()
    threading.Thread(target=API_3).start()
    threading.Thread(target=API_4).start()
    threading.Thread(target=API_5).start()
    threading.Thread(target=API_6).start()
    threading.Thread(target=API_7).start()
    threading.Thread(target=API_8).start()
    threading.Thread(target=API_9).start()
    threading.Thread(target=API_10).start()
    threading.Thread(target=API_11).start()
    threading.Thread(target=API_12).start()
    threading.Thread(target=API_13).start()
    threading.Thread(target=API_14).start()
    threading.Thread(target=API_15).start()