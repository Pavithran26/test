data = input("Enter binary data: ")

ones = data.count('1')

if ones % 2 == 0:
    parity_bit = '0'
else:
    parity_bit = '1'

transmitted = data + parity_bit

print("Original data:", data)
print("Parity bit:", parity_bit)
print("Transmitted data:", transmitted)

received = input("Enter received data: ")

if received.count('1') % 2 == 0:
    print("No error detected (even parity)")
else:
    print("Error detected")