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

#### dnsenum 

#### dig

#### nslookup 

``sh 
nslookup parrot-ctfs.com 
``

``sh
nslookup -query<type> parrot-ctfs.com 
``

record types: 
* MX
* TXT
* A
* CNAME
* AAA
* AAAA


### Pivoting Notes: 


