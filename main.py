from setuptools import setup, find_packages
import numpy as np
from mst_package import transpose2d

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transposed_matrix = transpose2d(matrix)
print(transposed_matrix)