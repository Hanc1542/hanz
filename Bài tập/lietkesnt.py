import math
def isPrimeNumber(n):
    if (n<2):
        return False
    squareRoot = int(math.sqrt(n))
    for i in range(2,squareRoot+1):
        if (n%2 == 0):
            return False
    return True
n = int(input("nhap so ngto "))
x = ""
dem = 0
i = 2 
while ( dem < n ):
    if (isPrimeNumber(i)):
        x = x + str(i) + ""
        dem = dem + 1
    i = i + 1
print(x)