#def number():
#    N = 10
#    B = [0] * N
#    for i in range(N):
#        B[i] = int(input("Введите число: "))
#    print(B)

#print(number())

def number2():
    i = 0
    N = 10
    B = [0] * N
    for i in range(N):
        B[i] = int(input("Введите число: "))
    B = sorted(B)
    print(B[9])



print(number2())
        
    