from pwn import *

"""
Binary gives a different output if you give it a substring
"""

import string

flag = "shaktictf{"

while True:
    found=False
    for c in string.printable:
        io = process('margaret')
        io.recvline()
        io.sendline(flag+c)
        try:
            if io.recvline(timeout=0.5) != b'Try Harder!!\n':
                flag+=c
                found=True
                break
        except:
            flag+=c
            found=True
            break
        io.close()
    if not found:
        break
    print(flag)
