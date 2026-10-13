"""Experiment 03: Measure latency, bandwidth, and throughput."""


def main():
    print("Network Performance Analysis")
    try:
        latency = float(input("Enter latency (ms): "))
        bandwidth = float(input("Enter bandwidth (Mbps): "))
        data_size = float(input("Enter data transferred (MB): "))
        transfer_time = float(input("Enter transfer time (seconds): "))
    except ValueError:
        print("Invalid input: please enter numeric values.")
        return

    if latency < 0 or bandwidth <= 0 or data_size < 0 or transfer_time <= 0:
        print("Invalid input: latency/data size must be non-negative, bandwidth and transfer time must be positive.")
        return

    throughput = data_size / transfer_time  # MB/s
    print("\n----- Results -----")
    print("Latency:", latency, "ms")
    print("Bandwidth:", bandwidth, "Mbps")
    print("Throughput:", round(throughput, 2), "MB/s")

    if throughput * 8 <= bandwidth:
        print("Throughput is within the available bandwidth.")
    else:
        print("Throughput exceeds the specified bandwidth.")

    if latency < 50:
        print("Latency Status: Low")
    elif latency <= 100:
        print("Latency Status: Moderate")
    else:
        print("Latency Status: High")


if __name__ == "__main__":
    main()
