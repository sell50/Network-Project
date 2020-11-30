# def findAllIP(ipSubnet: str):
#     for ip in ipaddress.IPv4Network(ipSubnet):
#         print(ip)
#
#         s = socket(AF_INET, SOCK_STREAM)
#         setdefaulttimeout(1)
#         result = s.connect_ex((str(ip), 80))
#         if (result == 0):
#             print('open !!!!!!!!!!!!!!!!!!!!!')
#         else:
#             print('closed' +str(ip))

import socket
import threading
import time
from queue import Queue

# DetectIpAddresses.py answers One-to-One Question 3. Detect all live IP addresses on a given subnet.
# The job description contains the target subnet in a.b.c.d/x format.

socket.setdefaulttimeout(0.25)
print_lock = threading.Lock()

target = input('Enter the host to be scanned: ')
t_IP = socket.gethostbyname(target)
print('Starting scan on host: ', t_IP)


# Function scans for open ports
def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((t_IP, port))
        with print_lock:
            print(port, 'is open')
        con.close()
    except:
        pass


def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()


q = Queue()
startTime = time.time()

for x in range(100):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(1, 500):
    q.put(worker)

q.join()
print('Time taken:', time.time() - startTime)

# findAllIP('192.168.1.0/24')
