def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    
    gcd, x1, y1 = extended_gcd(b % a, a)
    
    x = y1 - (b // a) * x1
    y = x1
    
    return gcd, x, y

# Sử dụng hàm để tính GCD và các hệ số Bézout của hai số
#Tinh b^-1 mod a
a = 6828*7392
b = 1564757
gcd, x, y = extended_gcd(a, b)
if y <0:
    y = y + a
print(f"GCD({a}, {b}) = {gcd}")
print(f"Hệ số Bézout: x = {x}, y = {y}")
print(f"{b}^-1 mod {a} = {y}")