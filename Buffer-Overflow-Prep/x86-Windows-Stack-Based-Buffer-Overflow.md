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

Resources: 

XP ISO FILE: https://archive.org/details/WinXPProSP3x86 <br />
PRODUCT KEY:  M6TF9-8XQ2M-YQK9F-7TBB2-XGG88

SNAPSHOT I CREATED: < will put on here when I find out where imma host it >

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

##### Demo 1

NOTES:  this is not valid python! This is Just a mind map, but very important to understand.

```python3 
string parrot(str):
     parrotbathing = parrotbathing()
     return parrotbathing

int main(): <-- this is a different part in memory than "string parrot" 
     str = "hello world" 
     parrot(str)
     program.continue
```

Explaination: 

when "main()" runs "str" will set "hello world" in the stack. Then it will hit the "parrot(str)" but it has to go somewhere else 
in memory to execute it so "program.continue" will save its place so it knows to come back to that same spot. "string parrot(str):"
will then be executed and when it hits "return parrotbathing" it will go back to program.continue

Order of everything being ran: 

```python3 
4. string parrot(str):
5.     parrotbathing = parrotbathing()
6.     return parrotbathing

1. int main(): <-- this is a different part in memory than "string parrot" 
2.     str = "hello world" 
3.     parrot(str)
7.     program.continue
```
### Stack Instructions

NOTES: the highest point in the stack is the lowest point in memory


Assembly has serveral instructions specifically designed to interact with the stack 

* PUSH < operand >; Example: PUSH EAX
      * Decrements ESP and then places the operand (a register, address etc.)
      onto the top of the stack ( The Stack Grows )
      * Example: Imagine you have a stack of plates and you add a plate the last plate you put on there is the first plate you are gonna take off 

* POP < operand >; Example: POP EAX
      * Loads the value from the top of the stack into the location specified in the operand then increments ESP ( The Stack Shrinks )
      * This does the opposite of PUSH 
* RET 
     * Transfers Program to control to a return address located on the top of
     the stack. Typically, this address is places on the stack by a CALL instruction when a function is called; This instruction is intended to return to a normal execution flow after a function is finished execution 


#### Demo 2

<img src="/images/immunity.png">

ASSEMBLY BREAK DOWN: 

* ( PUSH EBP - SUB ESP, 98 ) Adjusting stack pointers to make room in the stack for a new stack frame to operate in

* ( MOV EAX,DWORD PTR SS:[ EBP+8 ] - MOV DWORD PTR SS:[ ESP ],EAX ) Taking function paramaters and loading them onto the stack 

* Calling A function in C called strycpy which is a string copy function in C

* RETURNS 


### More on the stack ( smashing the stack )

#### Stack Mind Map

LINK: http://unixwiz.net/techtips/win32-callconv-asm.html

<img src="/images/stack.png" >

* ESP is the top of the stack 
* EBP is bottom of the CURRENT stack frame
* EIP saved right after EBP ( return address right here )
* Function arguments 

#### What is the purpose of learning all this stuff? 

* Some low level programing languages ( C and C++ mostly ) do not check how large data is before it puts it onto the stack 

* If user inpute is accepted into a variable the programmer must be sure
to include logic to check the supplied data and ensure it is apporpriately sized before it is accepted into the proccess memory and placed onto the stack 

* Many languages do  not have default protections 


Example Vulnerable Code: 

```c 
void main()
{
     char bufferA[50];
     char bufferB[16];

     printf("what is your name?\n");

     gets(bufferA);

     strcpy(bufferB, bufferA);
     return; 
}

```


## Buffer Overflow 

## Demo 

