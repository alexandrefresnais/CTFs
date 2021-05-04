"""
Calculates all rsi values taken
"""

def compute_all_rsi_values():
    # We start at rsi = 0
    rsi = 0
    arr = [0]
    rsi = (rsi * 0xb5 + 0xd9) % 0x200

    while rsi != 0:
        arr.append(rsi)
        rsi = (rsi * 0xb5 + 0xd9) % 0x200

    # We rotate the array so that RET is the last rsi value
    arr = arr[430:] + arr[:430]
    return arr


if __name__ == "__main__":
    arr = compute_all_rsi_values()
    print("Number of rsi values:", len(arr))
    print("Input to have all 512 instructions executed:", arr[0])
    print("ret is at index:", arr.index(0x9d))
