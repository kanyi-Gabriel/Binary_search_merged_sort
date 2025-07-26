# Binary Search with Merge Sort Implementation

This repository contains Python implementations of iterative binary search and merge sort algorithms. The program demonstrates how to efficiently search for elements in an unsorted array by first sorting it using merge sort, then applying binary search.

## 📋 Table of Contents
- [Features](#features)
- [How It Works](#how-it-works)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Example Output](#example-output)
- [Algorithm Complexity](#algorithm-complexity)
  


## 🚀 Features

- **Iterative Binary Search**: Efficient O(log n) search algorithm
- 
- **Merge Sort Implementation**: Stable O(n log n) sorting algorithm
- 
- **Complete Solution**: Automatically sorts unsorted data before searching
- 
- **Error Handling**: Returns -1 for elements not found in the array


## 💡 How It Works

1. **Input**: An unsorted array and target values to search for

3. **Sorting**: The array is sorted using merge sort algorithm
 
5. **Searching**: Binary search is applied to find the target values efficiently

7. **Output**: Returns the index positions of found elements or -1 if not found

## 🛠️ Prerequisites

- Python 3.x installed on your system

## ⚡ Algorithm Complexity
### Merge Sort
Time Complexity: O(n log n) in all cases (best, average, worst)

Space Complexity: O(n)

Stability: Stable sorting algorithm

### Binary Search
Time Complexity: O(log n)

Space Complexity: O(1) for iterative implementation

Requirement: Array must be sorted

## Example of sample output

   ```python

  Sorted Array: [32, 54, 64, 78, 90, 100, 123, 169]
  Target 54 found at index 1
  Target 123 found at index 6
  Target 189 not found in the array
