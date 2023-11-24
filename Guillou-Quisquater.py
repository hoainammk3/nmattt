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
# A
p = 991
u = 2343
# B
q = 839
# TA
b = 13367

n = p * q
v = modular_exponentiation(mod_inverse(u, n), b, n)

