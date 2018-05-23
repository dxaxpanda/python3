import nmap
import os

def main():
    for s in range(1, 255):
        ip = '192.168.1.{}'.format(s)
        print(ip)
        scanner(ip, '22-443')

def line_delimiter(x):
    print('-' * int(x))

# scanner function
def scanner(ip, port_range):
    nm = nmap.PortScanner()
    nm.scan(ip, port_range, arguments='-O')
    #while nm.still_scanning():
    #    print("Waiting ...")
    #    nm.wait(2)

    if (os.getuid() == 0):
        line_delimiter(20)
        if 'osclass' in nm[ip]:
            nm.scaninfo()
            for osclass in nm[ip]['osclass']:
                print('OsClass.type : {0}'.format(osclass['type']))
                print('OsClass.vendor : {0}'.format(osclass['vendor']))
                print('OsClass.osfamily : {0}'.format(osclass['osfamily']))
                print('OsClass.osgen : {0}'.format(osclass['osgen']))
                print('OsClass.accuracy : {0}'.format(osclass['accuracy']))

        if 'fingerprint' in nm[ip]:
            print('Fingerprint : {}'.format(nm[ip]['fingerprint']))

        print(nm.csv())

if __name__ == '__main__':
    main()
