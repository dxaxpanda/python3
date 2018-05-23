from socket import gethostbyname, gethostname, socket, AF_INET, SOCK_STREAM, SOCK_DGRAM, setdefaulttimeout
from threading import Thread

class Scanner(Thread):

    def __init__(self):
        setdefaulttimeout(1)
        Thread.__init__(self)

        self.open_ports = []

        # Ports from 1-65535
        self.ports = range(1, 0xffff + 1)
        self.host = gethostname()
        self.ip = gethostbyname(self.host)

    def scan(self, host, port):
        try:
            # Create a TCP socket and try to connect
            s = socket(AF_INET, SOCK_STREAM)
            s.connect((host, port))
            self.open_ports.append("Port %s is [Open] on host %s" % (port, host))
        except:
            pass

    def write(self):
        for op in self.open_ports:
            print(op)

    def run(self):
        self.threads = []

        # Enumerate our ports and scan
        for i, port in enumerate(self.ports):
            s = Thread(target=self.scan, args=(self.ip, port))
            s.start()
            self.threads.append(s)

        # Finish threads before main thread starts again
        for thread in self.threads:
            thread.join()

        # Write out the ports that are open
        self.write()

# Scanner object which initializes our vars and then we run our scanner
scanner = Scanner()
scanner.run()
