# link for LinkedIn post
https://www.linkedin.com/posts/shehla-kayani-b095b824a_github-shehla-ibrardsa-binary-and-linear-search-activity-7286618020456624129-Ur5N?utm_source=social_share_send&utm_medium=android_app&utm_campaign=copy_link
 
 # Binary Search 

This repository contains an implementation of the Binary Search algorithm in Python. The code performs a binary search on a sorted array to find a target element. The program returns the index of the target element if it is found, or `-1` if the element is not present in the array.

## Purpose

The purpose of this code is to demonstrate the binary search algorithm, which is an efficient search method for sorted arrays.
Further code explanation is given the program with each code line.

### How to Run the Program
### Prerequisites

- Python 3.x should be installed on your machine.

### Steps to Run

1.Directly copy the code from this folder and run on Anaconda Navigator

2. **Clone the repository** to your local machine

#### Time Complexity 
The time complexity of binay search program is O(log n) in average and best cases where n is the size of array
(Worst Case O(n))
Binary search runs O(n) in many cases such that the array is unsorted and very large, binary case not have a time complexity of O(n) in worst case as it is optimized for sorted arrays.The O(n) complexity will only apply when you are searching through unsorted array.

# Linear Search

Linear Search, also known as sequential search, is a straightforward algorithm used to find a specific element (the target) in a list or array.

## Purpose 
This program implements the Linear Search algorithm. Linear Search is a simple search algorithm that checks each element of a list sequentially until the target element is found or the entire list has been traversed.

### How to Run the Program

1. Copy the code: Ensure the Python code is copied into a file, for example, linear_search.py.

2.  Run the program: You can run the program using Python 3 by executing following command in terminal.

  python3 linear_search.py
  
4.  You can directly copy the code and run on an online compiler.

python3 linear_search.py



#### Purpose of the Code

This code searches for a specific target value within an array and returns the index at which the target is found. If the target is not found, the function returns -1.

Example output:

target found at index: 2

Further code explanation is given in the program.

#####  Time Complexity

The time complexity of Linear Search is O(n), where n is the number of elements in the array. In the worst case, the algorithm will search through the entire array.

Best Case: The target is found at the first position (O(1)).

Worst Case: The target is found at the last position or not found at all (O(n)).






