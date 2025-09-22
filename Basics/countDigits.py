from os import *
from sys import *
from collections import *
from math import *

def countDigit(n: int) -> int:
    
    if n == 0:
        return 1
    
    ans = 0
    while n != 0:
        ans += 1
        n = n // 10
    return ans



if __name__ == "__main__":
    num = int(input("Enter number: "))
    print(countDigit(num))
