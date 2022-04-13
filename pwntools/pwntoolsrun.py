from pwn import * 

p = process("/bin/sh")
p.sendline("echo here is your shell senpai parrot;")
p.interactive()

