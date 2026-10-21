print("Transmission Modes")
print("1. Simplex")
print("2. Half-Duplex")
print("3. Full-Duplex")

mode = int(input("Enter transmission mode (1-3): "))

signal_type = input("Enter signal type (Analog/Digital): ")
bits = int(input("Enter total number of bits transmitted: "))
time = float(input("Enter transmission time (in seconds): "))

bit_rate = bits / time
if mode == 1:
    mode_name = "Simplex"
elif mode == 2:
    mode_name = "Half-Duplex"
elif mode == 3:
    mode_name = "Full-Duplex"
else:
    mode_name = "Invalid Mode"

print("\n--- Transmission Analysis ---")
print("Transmission Mode :", mode_name)
print("Signal Type       :", signal_type)
print("Bits Transmitted  :", bits)
print("Time Taken        :", time, "seconds")
print("Bit Rate          :", bit_rate, "bps (bits per second)")