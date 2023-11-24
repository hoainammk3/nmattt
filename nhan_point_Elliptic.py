def point_addition(P, Q, a, p):
    if P == (0, 0):
        return Q
    if Q == (0, 0):
        return P

    x1, y1 = P
    x2, y2 = Q

    if P != Q:
        # Cộng hai điểm khác nhau trên đường cong
        s = ((y2 - y1) * pow(x2 - x1, -1, p)) % p
    else:
        # Cộng một điểm với chính nó
        s = ((3 * x1**2 + a) * pow(2 * y1, -1, p)) % p

    x3 = (s**2 - x1 - x2) % p
    y3 = (s * (x1 - x3) - y1) % p

    return (x3, y3)

def point_multiplication(P, n, a, p):
    result = (0, 0)  # Điểm ban đầu là điểm vô cực (0, 0)

    for i in range(n.bit_length()):
        if n & (1 << i):
            result = point_addition(result, P, a, p)
        P = point_addition(P, P, a, p)  # Nhân P với 2

    return result

# Đường cong y^2 = x^3 + ax + b (mod p)
a = 0
b = 2
p = 29148673317027192076803511224910340652601472910453342645855152923351075384612579   # Trường hữu hạn

# Điểm trên đường cong
P = (13432156294904909426285385488478688851186010294488969597225545582556288476931786 , 14189988397210980694201428087808441194640589511953694081485656677096838040746821 )
M = (9363755683903815048483318922354742120059832924248639292108232125408632225865209 , 22826407503161874149386798261088894665714883021806448141694231112539099653411571)
s = 7564 # Hằng số
k = 9384
B = point_multiplication(P, s, a, p)
M1 = point_multiplication(P, k, a, p)

kB =  point_multiplication(B, k, a, p)
M2 = point_addition(M, kB, a, p)

print(B)
print(M1)
print(M2)

