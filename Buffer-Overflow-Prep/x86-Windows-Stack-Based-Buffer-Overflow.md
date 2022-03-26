# x86 Windows Stack-Based Buffer Overflow

YouTube Tutorial: 
<br />
link: https://youtu.be/Z2pQuGmFNrM

## Intro to Exploit Development

### Lab Setup 

* Target Machine: Windows XP SP3 (x86)
     * Ensure DEP is set to "AlwaysOff" Just in Case
     * Immunity Debugger
     * Mona Modules
     * WarFTP v1.65
* Attacker Machine: Demon Linux 

CPU Registers: 

* General Purpose Registers 
* Segment Registers ( legacy )
* Flags, EIP
* Floating Point Unit Registers
* MMX Registers ( legacy )
* XXM Registers ( used sometimes )

EIP is going to be the most important


### EIP 


## x86 Assembly Primer

#### What is Assembly? 

* A low-level Programming Language 
* Used to Communicate with the microprocessor directly
* Specific to the processor family ( Intel, ARM, MIPs, etc.)
* Almost one-to-one correspondence with machine language 


#### Where is Assembly? 

* broad applications in all fields of computing
     * used for the optimization of software, debugging, and all other manners of low-level coding
     * as low as you can get without being 1 and 0 itself
* Infosec Uses: 
     * shell coding 
     * encoders 
     * memory manipulation 
     * execution hijacking/exploitation 


#### Why is Assembly? 

* Gateway to understanding: 
     * memory/processor exploitation 
     * reverse engineering
     * shellcode
     * everything else 
* Without a grasp of assembly, it will be nearly impossible to master any of these fields

#### Intel Architecture

* x86 
     * 32 bit CPU Registers
     * Very Small Management scale of only a theoretical 4GB RAM
* x86_64
     * An extension of x86 for 64-bit processors
     * 64 bit CPU Registers can access much more than 4GB RAM 17Billion GB of ram is what it can access and handle 


#### Why Bother With 32 Bit Systems? 

* Crawl, Walk, Then Run 
* Mastering x86 is virtually required to progress to more complex worlds like x86_64
* Almost all 64-bit machines can handle 32-bit applications
     * it is, for this reason, a lot of malware use 32 bit

#### Instruction Format

``
[label] mnemonic [opperands] [; comment] 
``

* Label: used to represent either an identifier or a constant 
* Mneumonic: identifies the purpose of the statement. a Mneumonoc is not required if a line contains only a label or a comment 
     Examples of mnemonic: 
     * PUSH 
     * ADD 
     * MOV
     * RENT
* Operands: specifies the data to be manipulated
     * most instructions take two of these 
* Comment: Literally Just a Comment 

add eax, ebx; EAX = EAX + EBX 

Important Note:
There are two types of syntax:
* AT&T
* Intel 

AT&T uses $ for const and % for Registers
AT&T goes source to destination while Intel does destination to source 


## Win32 Process Memory 

#### The basics of the Stack 

A stack is a place in the memory of a computer that holds Temporary Variables/Data

* When a application is initilized, Windows creates the proccess and assigns virtual memory to it 
* 32 bit proccesses have addresses that range from 0x00000000 to 0xFFFFFFFF
     * 0x00000000 - 0x7FFFFFFF is for user mode
     * 0x80000000 - 0xFFFFFFFF is for kernal mode 
* Windows uses the flat memory model 
     * Addresses are arranged in sequence 


#### Process Memory Mind Map

<img src=/images/proccess-memory.png width=300px height=300px>

<br />

#### What Is held in the Stack? 

* User input to be used later on by application
* Variables


#### Return Address 

For each new program function, A new stack frame is created. 
Close to the bottom of each stack frame, There is a return address 
the return address tells the CPU where to execute and where to go 
after it is done. 

##### Demo 


<p color="yellow"> Note:  this is not valid python! just a mind map </p>


```python3 
string parrotisgay(str):
     parrotbathing = parrotbathing()
     return parrotbathing

int main: # this is a different part in memory than "string parrotisgay" 
     str = "fuck me" 
     parrotisgay(str)

```



## Buffer Overflow 

## Demo 
