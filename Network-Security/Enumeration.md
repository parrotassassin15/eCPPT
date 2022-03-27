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
* dnsrecon

#### DIG

##### Regular Query

``
dig parrot-ctfs.com
``

##### Dig Zone Transfer
``
dig parrot-ctfs.com AXFR +noall +noanswer 
``

<img src="/images/dig.png">

#### NSLOOKUP 

``
nslookup parrot-ctfs.com 
``

``
nslookup -query=<type> parrot-ctfs.com 
``

<img src="/images/nslookup.png">

Record Types: 
* MX
* TXT
* A
* CNAME
* AAA
* AAAA

#### FIERCE

``
fierce --domain parrot-ctfs.com
``

<img src="/images/fierce.png">


#### DNSENUM

``
dnsenum -r parrot-ctfs.com
``

DNSENUM is a very powerful tool even going as far as to bruteforce subdomains 

### Host Discovery

``
fping -ag 192.168.0.1/24 2>/dev/null
``

``
nmap -v -sn 192.168.0.0/24
``

``
netdiscover -r 192.168.0.0/24
``

### Vulnerability Detection

#### Nmap + Searchsploit Automation 

``
nmap -sV -sC -A parrot-ctfs.com -oA parrot-ctfs-scan 
``

`` 
searchsploit --nmap parrot-ctfs-scan.xml
``
