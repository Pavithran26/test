"""Experiment 08: Character (byte) stuffing."""

FLAG = "F"
ESC = "E"


def character_stuffing(data):
    stuffed_data = FLAG
    for char in data:
        if char in (FLAG, ESC):
            stuffed_data += ESC
        stuffed_data += char
    stuffed_data += FLAG
    return stuffed_data


def main():
    data = input("Enter the data: ")
    result = character_stuffing(data)
    print("\nOriginal Data:", data)
    print("Stuffed Frame:", result)


if __name__ == "__main__":
    main()
