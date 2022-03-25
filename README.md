# eCPPT Notes

## System Security 

### Compiling on Windows 10 and Linux

C Code: 

```c
void funtest(int a, int b, int c) {
    int test1 = 55;
    int test2 = 56;
}
int main() {
    int x = 11;
    int z = 12;
    int y = 13;
    funtest(30,31,32);
    return 0;
}
```

#### Compile It: 

* Windows: PS> c1 functest.c
* Linux: ~# gcc functest.c -o hello_world

### Immunity Debugger Notes: 

#### Loading In A File:  

Click the folder Icon and load in the executable of your choice

#### Sections: ( Starting from the left )

Left Box has disassembled code which is divided into three sections:

* Section 1: Memory Address that contains the instruction 
* Section 2: Out Codes of the program
* Section 3: Assembaly Code 

Right Box has registries and their current values 

Bottom Left has three sections that contain the stack configuration 

* Section 1: Memory Address of the stack 
* Section 2: Hex code and values at that address
* Section 3: Acii representation 
* Section 4: Value contained there 

<!-- I will Finish this section off with a friend -->

## Network Security 

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


### Pivoting Notes: 

<!-- these are on a notpad -->
