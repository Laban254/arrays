import numpy as np
import array
import time
import sys

# Function to create test data
def create_data():
    # Creating a list
    my_list = [1, 2, 3, 4, 5]
    
    # Creating a NumPy array
    my_array = np.array([1, 2, 3, 4, 5])
    
    # Creating an array module array
    my_array_module = array.array('i', [1, 2, 3, 4, 5])
    
    return my_list, my_array, my_array_module

# Functions to test performance
def time_append_list(my_list):
    start_time = time.time()
    for i in range(10000):
        my_list.append(i)  # Appending elements to the list
    return time.time() - start_time

def time_append_numpy():
    my_array = np.array([1, 2, 3, 4, 5])
    start_time = time.time()
    for i in range(10000):
        my_array = np.append(my_array, i)  # Appending elements to NumPy array
    return time.time() - start_time

def time_append_array_module(my_array_module):
    start_time = time.time()
    for i in range(10000):
        my_array_module.append(i)  # Appending elements to array module array
    return time.time() - start_time

# Performance Testing
def performance_testing(my_list, my_array_module):
    list_time = time_append_list(my_list)
    numpy_time = time_append_numpy()
    array_module_time = time_append_array_module(my_array_module)

    print("Performance Testing Results:")
    print(f"Time taken to append to list: {list_time:.4f} seconds")
    print(f"Time taken to append to NumPy array: {numpy_time:.4f} seconds")
    print(f"Time taken to append to array module array: {array_module_time:.4f} seconds")

# Memory Testing
def memory_testing(my_list, my_array, my_array_module):
    list_memory = sys.getsizeof(my_list)
    numpy_memory = my_array.nbytes
    array_module_memory = sys.getsizeof(my_array_module)

    print("\nMemory Testing Results:")
    print(f"Memory size of list: {list_memory} bytes")
    print(f"Memory size of NumPy array: {numpy_memory} bytes")
    print(f"Memory size of array module array: {array_module_memory} bytes")

# Homogeneity Test
def homogeneity_test():
    mixed_list = [1, 2.5, '3', [4]]
    print("\nHomogeneity Test Result:")
    print(f"List with mixed types: {mixed_list}")

# Resizeability Test
def resizeability_test():
    # Creating an initial list
    dynamic_list = [1, 2, 3]
    print("\nResizeability Test:")
    
    # Check initial size
    print(f"Initial size of list: {len(dynamic_list)}")
    
    # Append elements
    for i in range(3, 8):
        dynamic_list.append(i)
    
    # Check new size
    print(f"Size after appending: {len(dynamic_list)}")

# Main execution
if __name__ == "__main__":
    my_list, my_array, my_array_module = create_data()
    
    performance_testing(my_list, my_array_module)
    memory_testing(my_list, my_array, my_array_module)
    homogeneity_test()
    resizeability_test()