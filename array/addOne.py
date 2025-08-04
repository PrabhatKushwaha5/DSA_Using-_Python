from os import *
from sys import *
from collections import *
from math import *

def addOneToNumber(arr):
    #   Write your code here
    result = int("".join(map(str,arr)))
    result += 1
    return [int(d) for d in str(result)]
    
