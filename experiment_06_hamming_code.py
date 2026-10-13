"""Experiment 06: Hamming Code (7,4) with single-bit error correction."""


def validate_bits(value, label, expected_length):
    if len(value) != expected_length or any(bit not in "01" for bit in value):
        raise ValueError(f"{label} must be exactly {expected_length} binary bits (0 or 1).")


def calculate_parity_bits(data):
    validate_bits(data, "Data", 4)
    hamming = ["0"] * 8  # Positions are numbered 1 through 7.
    data_index = 0
    for position in range(1, 8):
        if position not in (1, 2, 4):
            hamming[position] = data[data_index]
            data_index += 1
    for parity_position in (1, 2, 4):
        parity = 0
        for position in range(1, 8):
            if position & parity_position:
                parity ^= int(hamming[position])
        hamming[parity_position] = str(parity)
    return "".join(hamming[1:])


def detect_error(received):
    validate_bits(received, "Received Hamming code", 7)
    received_bits = ["0"] + list(received)
    error_position = 0
    for parity_position in (1, 2, 4):
        parity = 0
        for position in range(1, 8):
            if position & parity_position:
                parity ^= int(received_bits[position])
        if parity:
            error_position += parity_position
    return error_position, received_bits


def main():
    try:
        data = input("Enter 4 data bits: ").strip()
        hamming_code = calculate_parity_bits(data)
        print("\nGenerated Hamming Code:", hamming_code)

        received = input("\nEnter received Hamming Code (7 bits): ").strip()
        error_pos, received_bits = detect_error(received)
        if error_pos == 0:
            print("No error detected. Received data is correct.")
        else:
            print("Error detected at position:", error_pos)
            received_bits[error_pos] = "1" if received_bits[error_pos] == "0" else "0"
            print("Corrected Hamming Code:", "".join(received_bits[1:]))
    except ValueError as exc:
        print("Invalid input:", exc)


if __name__ == "__main__":
    main()
