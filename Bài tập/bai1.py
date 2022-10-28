def convert_number(n, b):
    if (n < 0 or b < 2 or b > 16):
        return "";
    sb = "";
    m = 0;
    remainder = n;
  
    while (remainder > 0):
        if (b > 10):
            m = remainder % b;
            if (m >= 10):
                sb = sb + str(chr(55 + m));
            else:
                sb = sb + str(m);
        else:
            sb = sb + str(remainder % b);
        remainder = int(remainder / b);
    return "".join(reversed(sb)); # đảo ngược chuỗi sb
  
n = int(input("Nhập số nguyên dương n = "));
print("Hệ cơ số 2 của số nguyên ", n, "là:", convert_number(n, 2))
print("Hệ cơ số 16 của số nguyên ", n, "là:", convert_number(n, 16))
