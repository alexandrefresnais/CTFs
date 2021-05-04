from rsi_values import compute_all_rsi_values

lines = []
with open('ordered') as my_file:
    for line in my_file:
        lines.append(line)

# Values taken by rsi for each instruction, in right order
arr = compute_all_rsi_values()

for i in range(70):
    # Get the unique value to the char
    xored_value = int(lines[16 + 7 * i].split(',')[1], 16)
    # Get RSI value at the XOR RSI instruction
    rsi_value = arr[17+7 * i]
    # Undo XOR
    char_value = xored_value ^ rsi_value
    # Undoing MOV BH,BL
    char_value = char_value % 0x100
    print(chr(char_value), end='')

