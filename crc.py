def xor_division(data, generator):
    bits = list(data)
    n = len(generator)

    for i in range(len(bits) - n + 1):
        if bits[i] == '1':
            for j in range(n):
                bits[i + j] = str(
                    int(bits[i + j]) ^ int(generator[j])
                )

    return ''.join(bits[-(n - 1):])


data = input("Enter data bits: ")
generator = input("Enter generator bits: ")

padded_data = data + '0' * (len(generator) - 1)
remainder = xor_division(padded_data, generator)

transmitted = data + remainder

print("CRC remainder:", remainder)
print("Transmitted data:", transmitted)

received = input("Enter received data: ")

check = xor_division(received, generator)

if all(bit == '0' for bit in check):
    print("No error detected")
else:
    print("Error detected")