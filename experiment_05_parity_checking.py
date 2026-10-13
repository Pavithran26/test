# EXPERIMENT 05: PARITY CHECKING FOR ERROR DETECTION
# Aim: To implement Even and Odd Parity generator and checking routines in Python to detect single-bit errors in transmission blocks.

data = input("Enter binary data: ")
print("\n1. Even Parity\n2. Odd Parity")
choice = int(input("Enter your choice: "))

ones = data.count('1')

if choice == 1:
    parity_bit = '0' if ones % 2 == 0 else '1'
    parity_type = "Even"
elif choice == 2:
    parity_bit = '1' if ones % 2 == 0 else '0'
    parity_type = "Odd"
else:
    print("Invalid choice")
    exit()

transmitted_data = data + parity_bit
print("\nParity Type:", parity_type)
print("Parity Bit:", parity_bit)
print("Transmitted Data:", transmitted_data)

# Receiver verification
received_data = input("\nEnter received data: ")
received_ones = received_data.count('1')

if choice == 1:
    if received_ones % 2 == 0:
        print("No error detected.")
    else:
        print("Error detected.")
elif choice == 2:
    if received_ones % 2 == 1:
        print("No error detected.")
    else:
        print("Error detected.")


============================================================
