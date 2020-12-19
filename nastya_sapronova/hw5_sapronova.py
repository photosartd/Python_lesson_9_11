def count():
    x = int(input("Введите любое число: "))
    m = 0 
    n = 0
    while x > 0:
        rest = x % 10
        if rest % 2 == 0:
            m = m + 1
        else:
            n = n + 1
        x = x//10    
    return (m, n)

def print_3_times(str1):
    for i in range(3):
        print(str1)

print_3_times("Saturday")
print("Hi")