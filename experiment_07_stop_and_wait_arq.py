"""Experiment 07: Stop-and-Wait ARQ simulation."""

import time


def stop_and_wait(frames, pause=0.5):
    if frames <= 0:
        raise ValueError("Number of frames must be a positive integer.")
    for frame in range(1, frames + 1):
        while True:
            print(f"\nSender: Sending Frame {frame}")
            time.sleep(pause)
            print(f"Receiver: Frame {frame} received successfully")
            time.sleep(pause)
            ack = input(f"Enter ACK for Frame {frame} (Y/N): ").strip().upper()
            if ack == "Y":
                print(f"Sender: ACK {frame} received")
                print(f"Frame {frame} transmitted successfully")
                break
            if ack == "N":
                print(f"Sender: ACK {frame} lost")
                print(f"Sender: Retransmitting Frame {frame}")
            else:
                print("Invalid ACK. Please enter Y or N.")
    print("\nAll frames transmitted successfully.")


def main():
    try:
        frames = int(input("Enter the number of frames: "))
        stop_and_wait(frames)
    except ValueError as exc:
        print("Invalid input:", exc)


if __name__ == "__main__":
    main()
