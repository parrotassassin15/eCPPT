# Lab Machine Write up and Notes 

## Resources: 

Orignal Exploit: https://www.exploit-db.com/exploits/3570


### Nmap of the XP Machine

<img src="/images/nmap-xp-machine-tcp.png" >

A quick Nmap scan of the target machines reviels tcp port 21 open. I also outputed to all formats 
so I can import into searchsploit to see if it catches some stuff. 

###  SearchSploit Results

I imported nmap scan like so: 

``
searchsploit --nmap xp-machine-tcp.xml 
``

But output was too versbose did not put it here and instead re ran the command manually 

<img src="/images/searchsploit-1.png" >


###  Metasploit Console Exploit

<img src="/images/msfconsole.png" >

As you can see the exploit did not work ( This is because it just crashed the application so we are gonna remake this mannually )

