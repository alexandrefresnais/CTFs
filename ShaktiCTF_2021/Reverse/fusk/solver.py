#shaktictf{s1mpl3_movfu5ca7i0n}

def rec(n):
    if (1 < n):
        i = rec(n-1)
        n = rec(n-2)
        return n+i
    return n

xored = [0x71,0x6b,0x64,0x63,0x79,0x7c,0x41,0x43,0x3f,0xeb,0x9a,
0x148, 0x20f, 0x3ab, 0x651, 0xa2b, 0x100a, 0x1a00, 0x2aad, 0x4559, 0x6f97, 0xb555, 0x12524,
0x1da52, 0x2ff23, 0x4d944, 0x7d8dc, 0xcb218, 0x148ab3, 0x213d78, 0x35c7e8]

for i in range(len(xored)):
    print(chr(xored[i] ^ rec(i+3)), end='')
