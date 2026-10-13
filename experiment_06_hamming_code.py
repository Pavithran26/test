# EXPERIMENT 06: HAMMING CODE (7, 4) FOR SINGLE-BIT ERROR DETECTION AND CORRECTION
# Aim: To implement Hamming Code (7, 4) in Python to compute redundant parity bits, locate erroneous bit positions using syndrome bits, and automatically correct errors.

def calculate_parity_bits(data):
    m = len(data)
    r = 0
    while (2 ** r) < (m + r + 1):
        r += 1
    n = m + r
    hamming = ['0'] * (n + 1)
    j = 0
    for i in range(1, n + 1):
        if (i & (i - 1)) != 0:
            hamming[i] = data[j]
            j += 1
    for p in range(r):
        position = 2 ** p
        parity = 0
        for i in range(1, n + 1):
            if i & position:
                parity ^= int(hamming[i])
        hamming[position] = str(parity)
    return "".join(hamming[1:])

def detect_error(received):
    n = len(received)
    received = ['0'] + list(received)
    error_position = 0
    position = 1
    while position <= n:
        parity = 0
        for i in range(1, n + 1):
            if i & position:
                parity ^= int(received[i])
        if parity != 0:
            error_position += position
        position *= 2
    return error_position, received

data = input("Enter data bits: ")
hamming_code = calculate_parity_bits(data)
print("\nGenerated Hamming Code:", hamming_code)

received = input("\nEnter received Hamming Code: ")
error_pos, rec_data = detect_error(received)

if error_pos == 0:
    print("No error detected. Received data is correct.")
else:
    print("Error detected at position:", error_pos)
    rec_data[error_pos] = '1' if rec_data[error_pos] == '0' else '0'
    print("Corrected Hamming Code:", "".join(rec_data[1:]))


============================================================
