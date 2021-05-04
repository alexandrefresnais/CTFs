from rsi_values import compute_all_rsi_values

"""
`instructions` file contains all instruction in the order given by Ghidra
without NOPs and without jumps
"""
lines = []
with open('instructions') as my_file:
    for line in my_file:
        lines.append(line)

# Values taken by rsi for each instruction, in right order
arr = compute_all_rsi_values()

# Reorder lines
f = open('ordered', 'w')
for i in range(512):
    f.write(lines[arr[i]])
f.close()
