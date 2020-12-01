import socket
import threading
import time
from queue import Queue

class DetectLiveIPAddress(object):
  
  def __init__(self):
    socket.setdefaulttimeout(0.25)
    print_lock = threading.Lock()    
  
  def detectIpAddresses(self, IPAddress):
    t_IP = socket.gethostbyname(IPAddress)
    print('Starting scan on host: ', t_IP)
    
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


# Function scans for open ports
def portscan(self, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((t_IP, port))
        with print_lock:
            print(port, 'is open')
        con.close()
    except:
        pass


def threader(self):
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()
        
def main(self):
  self.detectIPAddresses("1.1.1.1")

if __name__ == "__main__"
  obj = DetectLiveIPAddress()
  obj.main()
