num = int(input("Введите число: "))
def r(n):
  k=0
  for i in n:
     k+=not int(i)%2
  return k
num = input('n=')
print(r(num))



