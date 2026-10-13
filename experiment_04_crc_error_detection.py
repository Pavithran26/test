"""Experiment 04: Cyclic Redundancy Check (CRC) error detection."""


def validate_bits(value, label):
    if not value or any(bit not in "01" for bit in value):
        raise ValueError(f"{label} must be a non-empty binary string containing only 0 and 1.")


def crc_division(data, generator):
    """Return the modulo-2 division remainder for data using generator."""
    validate_bits(data, "Data")
    validate_bits(generator, "Generator")
    if len(generator) < 2 or generator[0] != "1" or generator[-1] != "1":
        raise ValueError("Generator must be at least 2 bits long and start and end with 1.")
    if len(data) < len(generator):
        raise ValueError("Data must be at least as long as the generator.")

    work = list(data)
    for i in range(len(work) - len(generator) + 1):
        if work[i] == "1":
            for j, bit in enumerate(generator):
                work[i + j] = str(int(work[i + j]) ^ int(bit))
    return "".join(work[-(len(generator) - 1):])


def main():
    try:
        data = input("Enter data bits: ").strip()
        generator = input("Enter generator bits: ").strip()
        validate_bits(data, "Data")
        validate_bits(generator, "Generator")
        if len(generator) < 2 or generator[0] != "1" or generator[-1] != "1":
            raise ValueError("Generator must be at least 2 bits long and start and end with 1.")
        appended_data = data + "0" * (len(generator) - 1)
        remainder = crc_division(appended_data, generator)
        transmitted_data = data + remainder
        print("\nCRC Remainder:", remainder)
        print("Transmitted Data:", transmitted_data)

        received_data = input("\nEnter received data: ").strip()
        validate_bits(received_data, "Received data")
        if len(received_data) < len(generator):
            raise ValueError("Received data must be at least as long as the generator.")
        check_remainder = crc_division(received_data, generator)
        print("Checking Remainder:", check_remainder)
        if "1" in check_remainder:
            print("Error detected in received data.")
        else:
            print("No error detected. Data received correctly.")
    except ValueError as exc:
        print("Invalid input:", exc)


if __name__ == "__main__":
    main()
