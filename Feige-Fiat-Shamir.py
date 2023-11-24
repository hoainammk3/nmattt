def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)
# return u^-1 mod n
def mod_inverse(u, n):
    g, x, _ = extended_gcd(u, n)
    if g != 1:
        raise Exception('u không phải là số nguyên tố cùng nhau với n')
    else:
        return x % n

# return base ^ exponent mod modulus
def modular_exponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus  # Chắc chắn rằng base nằm trong phạm vi modulo
    
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result
p = 6829 
q = 7393
n = p*q
s1 = 157
s2 = 43215
s3 = 4646
b1 = 1 
b2 = 0
b3 = 1
v1 = (-1 ** b1) * mod_inverse(s1**2, n)
v1 = v1 % n