## x86 Windows Stack-Based Buffer Overflow

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

EIP is gonna be the most important


### EIP 


## x86 Assembly Primer

#### What is Assembly? 

* A low level Programming Language 
* Used to Comunicate with the microproccessor directly
* Specific to the proccessor family ( Intel, ARM, MIPs, etc.)
* Almost one-to-one corresponsence with machine language 


#### Where is Assembly? 

* broad applications in all fields of computing
     * used for optimization of software, debugging, and all other manner of low level coding
     * as low as you can get without being 1 and 0 itself
* Infosec Uses: 
     * shell coding 
     * encoders 
     * memory manipulation 
     * execution hijacking / exploitation 


#### Why is Assembly? 

* Gateway to understanding: 
     * memory/proccessor exploitation 
     * reverse engineering
     * shellcoding
     * everything else 
* Without a grasp of assembly, it will be nearly impossible to master any of these fields


## Win32 Process Memory 

## Buffer Overflow 

## Demo 
