rest % 2 == 0
if rest % 2 == 0
def ds():
    odd = 0
    even = 0
    while num > 0:
        rest = num % 10
        k = rest % 2
        if (k == 0): 
            even = even +1 
        else:
            odd = odd + 1
        num = num / 10
    print (even)
    print (" ")
    print (odd)
    return odd
num = int(input("Введите число: "))
odd1 = ds()