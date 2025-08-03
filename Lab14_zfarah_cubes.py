"""
Lab 14: Cube Graphs
Author: Zakarie Farah
This program creates a graph of the cubes of numbers.
First, it shows a bar chart of the first five cubes using a list.
Then, it automatically generates and plots the first 5000 cubes.
Date: August 2, 2025
"""

import matplotlib.pyplot as plt

numbers = [1, 2, 3, 4, 5]
cubes = [num**3 for num in numbers]

plt.figure(figsize=(6, 4))
plt.bar(numbers, cubes, color='skyblue')
plt.title("Cubes of First 5 Numbers")
plt.xlabel("Number")
plt.ylabel("Cube")
plt.grid(True)
plt.tight_layout()
plt.show()

big_numbers = list(range(1, 5001))
big_cubes = [num**3 for num in big_numbers]

plt.figure(figsize=(10, 4))
plt.plot(big_numbers, big_cubes, linewidth=1, color='purple')
plt.title("Cubes of Numbers 1 to 5000")
plt.xlabel("Number")
plt.ylabel("Cube")
plt.grid(True)
plt.tight_layout()
plt.show()
