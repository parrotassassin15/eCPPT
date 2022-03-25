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
```
~# nslookup 
> set q=txt
> parrot-ctfs.com
Server:  dns-cac-lb-02.rr.com
Address:  2001:1998:f00:2::1 

Non-authoritative answer:
parrot-ctfs.com text =

        "google-site-verification=TjhofXVN6L2Sx3XZ13UjKrWrGdurwLej9GwNbJNA8bc"
parrot-ctfs.com text =

        "google-site-verification=no20CHIMfmEkXmLm1mtHyHKSC3x1b3tUk3sTrwFy8OU"
parrot-ctfs.com text =

        "v=spf1 mx ip4:192.223.26.241 include:aspmx.googlemail.com include:_spf.google.com ~all"
> set q=mx
> parrot-ctfs.com
Server:  dns-cac-lb-02.rr.com
Address:  2001:1998:f00:2::1

Non-authoritative answer:
parrot-ctfs.com MX preference = 10, mail exchanger = alt3.aspmx.l.google.com
parrot-ctfs.com MX preference = 5, mail exchanger = alt1.aspmx.l.google.com
parrot-ctfs.com MX preference = 1, mail exchanger = aspmx.l.google.com
parrot-ctfs.com MX preference = 5, mail exchanger = alt2.aspmx.l.google.com
parrot-ctfs.com MX preference = 10, mail exchanger = alt4.aspmx.l.google.com
>
```

Record Types: 
* MX
* TXT
* A
* CNAME
* AAA
* AAAA

