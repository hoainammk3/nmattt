def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    
    gcd, x1, y1 = extended_gcd(b % a, a)
    
    x = y1 - (b // a) * x1
    y = x1
    
    return gcd, x, y

def find_e(p, q):
    a = (p-1)*(q-1)
    for i in range(a, 1000000, -1):
        gcd, x, y = extended_gcd(a, i)
        if gcd == 1:
            print(i)
            return i;        
    
def modular_exponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus  # Chắc chắn rằng base nằm trong phạm vi modulo
    
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
        
    return result

def RSA_findY(x, p, q, e):
    n = p * q
    y = modular_exponentiation(x, e, n)
    print("y = ", y)
    return y

def RSA_findX(y, p, q, e):
    phi_n = (p-1)*(q-1)
    n = q * p
    gcd, x2, y2 = extended_gcd(phi_n, e)
    if (y2 < 0):
        y2 = y2 + phi_n
    d = y2
    print("d = ", d)
    x = modular_exponentiation(y, d, n)
    print("x = ", x)
    return x
    
# 126555309557584758
# 126555 -> y = 5467538
# 309557 -> y = 2022092
# 584758 -> y = 5218157
# d =  5096895
# 128 ?

p = 5955301492186055123
q = 2729752695892102379
e = 6377991397696915908006317126519
x = 7473885996428194074
y = RSA_findY(x, p, q, e)
RSA_findX(y, p, q, e)