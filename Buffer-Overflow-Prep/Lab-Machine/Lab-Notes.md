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

#### Python One Liner To Find Crashing Point Manually

This prints 1,000 As for ease of access 

<img src="/images/python-oneliner.png">

#### In the case of trying this directly through a FTP Client on a modern Distrobution the Client will stop you from sending the max buffer 

<img src="/images/failed-exploit.png">

#### So we are going to try with NetCat and See if that works better 

<img src="/images/crash-succeeded.png">

#### As you can see we crashed the program ( I did have to enter a pass before it crashed ) and to confirm the crash opened our debugger 

<img src="/images/immunity-crash.png" width=812px height=474px>
