#!/usr/bin/env python3

import sys
from collections import defaultdict

# Initialize dictionaries to store values from matrices A and B
a_values = defaultdict(float)
b_values = defaultdict(float)

current_key = None
current_result = 0.0

# Read input from stdin (output from mapper)
for line in sys.stdin:
    # Remove leading and trailing whitespaces
    line = line.strip()
    
    # Split by tab to get key and value
    key, value = line.split('\t')
    
    # Parse the value
    parts = value.split(',')
    matrix_id = parts[0]
    index = int(parts[1])  # Column index for A, row index for B
    element_value = float(parts[2])
    
    # If we encounter a new key
    if current_key is not None and current_key != key:
        # Calculate dot product for the previous key
        result = sum(a_values[j] * b_values[j] for j in range(len(a_values)))
        
        # Emit the result
        print(f"{current_key} {result}")
        
        # Reset for new key
        a_values = defaultdict(float)
        b_values = defaultdict(float)
        current_result = 0.0
    
    # Update current key
    current_key = key
    
    # Store the value in the appropriate dictionary
    if matrix_id == 'A':
        a_values[index] = element_value
    else:  # matrix_id == 'B'
        b_values[index] = element_value

# Don't forget to output the last key
if current_key:
    result = sum(a_values[j] * b_values[j] for j in range(len(a_values)))
    print(f"{current_key} {result}")