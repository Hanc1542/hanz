def ucln(a,b):
    if (b == 0):
        return a
    return ucln(b,a%b)
def bcnn(a,b):
    return int((a*b)/ucln(a,b))
a = int(input())
b = int(input())
print("UCLN: ",ucln(a,b))
print("BCNN: ",bcnn(a,b))