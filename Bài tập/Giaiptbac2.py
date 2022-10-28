import math
def giaiPTbac2(a,b,c):
    if (a == 0):
        if (b == 0):
            print("Phuong trinh vo nghiem")
        else:
            print("Nghiem cua phuong trinh: ",-(c/b))
        return
    delta = b*2-4*a*c
    if (delta > 0):
        x1 = float((-b+math.sqrt(delta))/(2*a))
        x2 = float((-b-math.sqrt(delta))/(2*a))
        print("Phuong trinh co 2 nghiem: ", x1, x2)
    elif (delta == 0):
        x = (-b/(2*a))
        print("Phuong trinh co nghiem kep: ",x)
    elif (delta < 0):
        print ("Phuong trinh vo nghiem")
a = float(input())
b = float(input())
c = float(input())
giaiPTbac2(a,b,c)

        