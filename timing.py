import time
import random
from BSPTree import BSPTreeBuilder, Segment
import matplotlib.pyplot as plt
import numpy as np

# Function to generate random points
def generate_random_points(num_points):
    points = []
    for _ in range(num_points):
        x, y = random.uniform(0, 100), random.uniform(0, 100)
        points.append((x, y))
    return points

# Function to generate random segments from points
def generate_random_segments(num_segments):
    points = generate_random_points(num_segments * 2)
    segments = []
    for i in range(0, len(points), 2):
        segments.append(Segment(points[i], points[i + 1]))
    return segments

# List to store timing results
results = []

# Test with different input sizes
for n in range(10, 300, 10):
    raw_segments = generate_random_segments(n)

    start_time = time.perf_counter()
    bsp_tree_builder = BSPTreeBuilder(raw_segments)
    bsp_tree_builder = BSPTreeBuilder(raw_segments)
    bsp_tree_builder = BSPTreeBuilder(raw_segments)
    bsp_tree_builder = BSPTreeBuilder(raw_segments)
    bsp_tree_builder = BSPTreeBuilder(raw_segments)
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time / 5
    results.append((n, elapsed_time))
    print(f"Segments: {n}, Time: {elapsed_time:.6f} seconds")

# Prepare data for plotting
sizes = [r[0] for r in results]
times = [r[1] for r in results]

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(sizes, times, marker='o', label='Measured Time')
plt.xlabel('The number of random segments')
plt.ylabel('Time (seconds)')
plt.title('BSP Tree Construction Time Complexity')
plt.grid(True)
plt.legend()
plt.show()
