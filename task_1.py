import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt

# Function to measure execution time
def measure_execution_time():
    results = []

    # Test for different array lengths
    for n in range(1000, 100001, 1000):
        arr = np.random.randint(0, 100000, n)

        start_time = time.time()
        result = find_min_max(arr)
        end_time = time.time()

        execution_time = end_time - start_time
        results.append((n, execution_time, result))

    # Save results to a DataFrame
    df = pd.DataFrame(results, columns=["Array Length", "Execution Time", "Last Result"])
    return df

# Function to find min and max using divide and conquer
def find_min_max(arr):
    def divide_and_conquer(arr, low, high):
        if low == high:  # Single element in the subarray
            return arr[low], arr[low]

        if high == low + 1:  # Two elements in the subarray
            return (min(arr[low], arr[high]), max(arr[low], arr[high]))

        mid = (low + high) // 2

        left_min, left_max = divide_and_conquer(arr, low, mid)
        right_min, right_max = divide_and_conquer(arr, mid + 1, high)

        return min(left_min, right_min), max(left_max, right_max)

    if arr.size == 0:
        raise ValueError("Empty array is not allowed")

    return divide_and_conquer(arr, 0, len(arr) - 1)

# Generate and save execution times
df = measure_execution_time()

# Print the last result
total_rows = df.shape[0]
last_result = df.iloc[total_rows - 1]
print("Last Execution:")
print(f"Array Length: {last_result['Array Length']}")
print(f"Execution Time: {last_result['Execution Time']:.6f} seconds")
print(f"Result (Min, Max): {last_result['Last Result']}")

# Polynomial fitting and plotting
x = df["Array Length"]
y = df["Execution Time"]

# Fit a polynomial of degree 1 (linear)
coefficients = np.polyfit(x, y, 1)
polynomial = np.poly1d(coefficients)

# Generate fitted values
y_fit = polynomial(x)

# Plot results
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color="blue", label="Measured Times")
plt.plot(x, y_fit, color="red")
plt.xlabel("Array Length")
plt.ylabel("Execution Time (s)")
plt.title("Execution Time vs Array Length")
plt.legend(["Measured Times", "Fitted Line"], loc="best")
plt.grid()

# Save the figure
plt.savefig("execution_time_vs_array_length.png")
plt.show()
