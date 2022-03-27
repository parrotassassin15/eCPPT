## ENUMERATION 

### Whois Lookup 

Whois Lookup: 

* whois ( windows and linux )
* whois.icann.org/en

### Information Gathering DNS

DNS Enumeration: 

* dnsenum
* dig
* feirce
* nslookup 

#### DIG

``
dig parrot-ctfs.com
``



#### NSLOOKUP 

``
nslookup parrot-ctfs.com 
``

``
nslookup -query=<type> parrot-ctfs.com 
``

<img src="/images/nslookup.png>

Record Types: 
* MX
* TXT
* A
* CNAME
* AAA
* AAAA


#### Nmap + Searchsploit Automation 

``
nmap -sV -sC -A parrot-ctfs.com -oA parrot-ctfs-scan 
``

`` 
searchsploit --nmap parrot-ctfs-scan.xml
``


