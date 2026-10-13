"""Experiment 05: Even and odd parity error detection."""


def validate_bits(value, label):
    if not value or any(bit not in "01" for bit in value):
        raise ValueError(f"{label} must be a non-empty binary string containing only 0 and 1.")


def main():
    try:
        data = input("Enter binary data: ").strip()
        validate_bits(data, "Data")
        print("\n1. Even Parity\n2. Odd Parity")
        choice = int(input("Enter your choice: "))
        if choice not in (1, 2):
            print("Invalid choice")
            return

        ones = data.count("1")
        if choice == 1:
            parity_bit, parity_type = ("0" if ones % 2 == 0 else "1"), "Even"
        else:
            parity_bit, parity_type = ("1" if ones % 2 == 0 else "0"), "Odd"

        transmitted_data = data + parity_bit
        print("\nParity Type:", parity_type)
        print("Parity Bit:", parity_bit)
        print("Transmitted Data:", transmitted_data)

        received_data = input("\nEnter received data: ").strip()
        validate_bits(received_data, "Received data")
        received_ones = received_data.count("1")
        has_correct_parity = (received_ones % 2 == 0) if choice == 1 else (received_ones % 2 == 1)
        print("No error detected." if has_correct_parity else "Error detected.")
    except ValueError as exc:
        print("Invalid input:", exc)


if __name__ == "__main__":
    main()
