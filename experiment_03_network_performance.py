# EXPERIMENT 03: MEASURE AND COMPARE LATENCY, BANDWIDTH, AND THROUGHPUT
# Aim: To calculate, analyze, and compare network performance metrics including latency, throughput, and available transmission bandwidth using Python.

print("Network Performance Analysis")

# Input parameters
latency = float(input("Enter latency (ms): "))
bandwidth = float(input("Enter bandwidth (Mbps): "))
data_size = float(input("Enter data transferred (MB): "))
time = float(input("Enter transfer time (seconds): "))

# Calculate throughput
throughput = data_size / time

# Display results
print("\n----- Results -----")
print("Latency:", latency, "ms")
print("Bandwidth:", bandwidth, "Mbps")
print("Throughput:", round(throughput, 2), "MB/s")

# Compare bandwidth and throughput
if throughput * 8 <= bandwidth:
    print("Throughput is within the available bandwidth.")
else:
    print("Throughput exceeds the specified bandwidth.")

# Latency status classification
if latency < 50:
    print("Latency Status: Low")
elif latency <= 100:
    print("Latency Status: Moderate")
else:
    print("Latency Status: High")


============================================================
