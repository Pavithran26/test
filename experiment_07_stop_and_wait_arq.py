# EXPERIMENT 07: STOP-AND-WAIT SLIDING WINDOW PROTOCOL SIMULATION
# Aim: To simulate the Stop-and-Wait flow control and ARQ reliable data transfer mechanism with timeout retransmissions and acknowledgments using Python.

import time

def stop_and_wait(frames):
    for i in range(1, frames + 1):
        while True:
            print(f"\nSender: Sending Frame {i}")
            time.sleep(0.5)
            print(f"Receiver: Frame {i} received successfully")
            time.sleep(0.5)
            ack = input(f"Enter ACK for Frame {i} (Y/N): ").upper()
            if ack == 'Y':
                print(f"Sender: ACK {i} received")
                print(f"Frame {i} transmitted successfully")
                break
            else:
                print(f"Sender: ACK {i} lost")
                print(f"Sender: Retransmitting Frame {i}")
    print("\nAll frames transmitted successfully.")

# Input total frames and execute simulation
n = int(input("Enter the number of frames: "))
stop_and_wait(n)


============================================================
