def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def modular_exponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus  # Chắc chắn rằng base nằm trong phạm vi modulo
    
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

# Sử dụng hàm để tính GCD và các hệ số Bézout của hai số
#Tinh b^-1 mod a
a = 4050*4566
b = 1234567
gcd, x, y = extended_gcd(a, b)
if y <0:
    y = y + a
print(f"GCD({a}, {b}) = {gcd}")
print(f"Hệ số Bézout: x = {x}, y = {y}")
print(f"{b}^-1 mod {a} = {y}")

# Sử dụng hàm để tính b^n mod m
