def phantichsongto(n):
    i = 2
    listnumber = []
    while (n>1):
        if (n % i == 0):
            n = int(n/i)
            listnumber.append(i)
        else :
            i=i+1
    if (len(listnumber) == 0):
        listnumber.append(n)
    return listnumber
n = int(input("Nhap so: "))
listnumbers = phantichsongto(n)
size = len(listnumbers)
x = " "
for i in range(1,size):
    x = x + str(listnumbers[i]) + "x"
x = x + str(listnumbers[size-1])
print (x)
