#!/usr/bin/env python3

import sys

# Matrix dimensions
# For a 2x2 matrix multiplication
m = 2  # Number of rows in Matrix A
n = 2  # Number of columns in Matrix A / Number of rows in Matrix B
p = 2  # Number of columns in Matrix B

# Read each line from stdin (standard input)
for line in sys.stdin:
    # Remove leading and trailing whitespaces
    line = line.strip()
    
    # Split the line by comma
    parts = line.split(',')
    
    # Extract matrix ID, row index, column index, and value
    matrix_id = parts[0]
    i = int(parts[1])  # Row index
    j = int(parts[2])  # Column index
    value = float(parts[3])  # Value at the position
    
    # For matrix multiplication, we need to emit key-value pairs
    # For matrix A with dimensions m×n and matrix B with dimensions n×p
    # The resulting matrix C will have dimensions m×p
    
    if matrix_id == 'A':
        # For each element A[i,j], emit key-value pairs for all cells in row i of resulting matrix
        for k in range(p):
            # Key: position in the result matrix (i,k)
            # Value: matrix_id, column index j for joining with B, and the value
            output_key = f"{i},{k}"
            output_value = f"A,{j},{value}"
            print(f"{output_key}\t{output_value}")
    
    elif matrix_id == 'B':
        # For each element B[i,j], emit key-value pairs for all cells in column j of resulting matrix
        for k in range(m):
            # Key: position in the result matrix (k,j)
            # Value: matrix_id, row index i for joining with A, and the value
            output_key = f"{k},{j}"
            output_value = f"B,{i},{value}"
            print(f"{output_key}\t{output_value}")