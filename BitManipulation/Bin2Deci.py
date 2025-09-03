def Bin2Deci(x: str) -> int:
    deci_no = 0
    power = 0
    index = len(x) - 1
    while index >= 0:
        num = int(x[index]) * (2 ** power)
        deci_no += num
        index -= 1
        power += 1
    return deci_no


if __name__ == "__main__":
    x = input("Enter a binary number: ")
    print("Decimal equivalent:", Bin2Deci(x))
