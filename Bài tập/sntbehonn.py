import math

def IsPrimeNumber(n):
    # Nếu n<2 thì không phải số ngto
    if (n<2):
        return False
    squareroot = int(math.sqrt(n))
    for i in range(2,squareroot+1):
        if (n % i == 0):
            return False
    return True
n = int(input("Nhap n= "))
print("So nguyen to nho hon ",n,"la: ")
x = ""
if (n>=2) :
    x = x + " 2" + ""
for i in range(3,n):
    if (IsPrimeNumber(i)):
        x = x + str(i) + ""
    i = i + 2
print(x)


