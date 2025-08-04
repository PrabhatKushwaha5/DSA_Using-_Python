from os import *
from sys import *
from collections import *
from math import *

def rotate(arr, n):
    # Write your 
    arr[:] = [arr[-1]] + arr[:n-1]
    return " ".join(map(str,arr))