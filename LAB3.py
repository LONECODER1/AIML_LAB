# Q1
# a
# import numpy as np
# empty_arr = np.empty((3, 4))
# print(empty_arr)

# b
# import numpy as np
# full_arr = np.full((3, 4),5)
# print(full_arr)

# c
# import numpy as np
# full_arr = np.full((3, 4), 5.5, dtype=float)
# print(full_arr)
# print(full_arr.dtype) 

# Q2
# a
# import numpy as np
# full_arr=np.zeros(5)
# print(full_arr)

# # b
# import numpy as np
# full_arr=np.zeros((3,4))
# print(full_arr)

# c
# import numpy as np
# full_arr = np.zeros((3, 4), dtype=int)
# print(full_arr)
# print(full_arr.dtype) 

# d
# import numpy as np
# # Define tuple data type (e.g., two fields: int and float)
# dtype = [('id', 'i4'), ('value', 'f4')]
# # Create a NumPy array with tuple data type and zeros
# arr = np.zeros(5, dtype=dtype)
# print(arr)

# import numpy as np

# # -------------------------
# # 3. Check whether specified values are present in NumPy array
# # -------------------------
# print("=== Task 3: Check Values in NumPy Array ===")
# arr = np.array([1, 2, 3, 4, 5])
# values_to_check = [2, 6]

# for val in values_to_check:
#     if val in arr:
#         print(f"{val} is present in the array.")
#     else:
#         print(f"{val} is NOT present in the array.")

# # Vectorized check
# print("Vectorized check:", np.isin(values_to_check, arr))

# # -------------------------
# # 4. Fibonacci Series using Binet Formula
# # -------------------------
# print("\n=== Task 4: Fibonacci Series using Binet Formula ===")

# def fibonacci_binet(n):
#     phi = (1 + np.sqrt(5)) / 2
#     psi = (1 - np.sqrt(5)) / 2
#     return np.round((phi**n - psi**n) / np.sqrt(5)).astype(int)

# # (a) First 5 Fibonacci numbers
# n = np.arange(5)
# fib5 = fibonacci_binet(n)
# print("First 5 Fibonacci numbers:", fib5)

# # (b) First 'num' Fibonacci numbers
# num = 10
# n = np.arange(num)
# fib_n = fibonacci_binet(n)
# print(f"First {num} Fibonacci numbers:", fib_n)

# # -------------------------
# # 5. All 2D diagonals of a 3D NumPy array
# # -------------------------
# print("\n=== Task 5: 2D diagonals of a 3D NumPy array ===")
# arr3d = np.arange(3*3*3).reshape(3, 3, 3)
# print("3D array:\n", arr3d)

# diagonals = np.diagonal(arr3d, axis1=1, axis2=2)
# print("All 2D diagonals:\n", diagonals)
#Done

