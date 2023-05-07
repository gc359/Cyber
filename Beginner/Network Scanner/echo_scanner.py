
import subprocess
 
 
'''
ICMP Echo Request
It is also known by using ‘ping command’. An ICMP packet is sent to a host using the IP address and if the ICMP echo is received, that means that the host is online and is receiving the signals. For this, it necessary to get all the IP addresses for which you wish to test that the host is connected or not. This method works on the assumption that network devices have ICMP enabled.
''' 

for ping in range(1,10):
    address = "127.0.0." + str(ping)
    res = subprocess.call(['ping', '-c', '3', address])
    if res == 0:
        print( "ping to", address, "OK")
    elif res == 2:
        print("no response from", address)
    else:
        print("ping to", address, "failed!")
        
'''
This code iterates over all the available IP addresses, ping them and check for the reply. If the echo is received, that means the host is connected and in case, no echo is received, then it looks like that the host is down.
Note: Personal firewalls or general firewalls are often set to so called “stealth mode” which is used not to react to ICMP echo requests.
'''

'''
Sources: https://www.geeksforgeeks.org/network-scanner-in-python/
'''