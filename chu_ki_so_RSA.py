def modular_exponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus  # Chắc chắn rằng base nằm trong phạm vi modulo
    
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y
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

def maHoaTen(name, coSo):
    res = 0
    for i in range (len(name) -1, -1, -1):
        a = char_to_number(name[i])
        res =res + a * pow(coSo, len(name)-i-1)
    return res
def char_to_number(char):
    if 'a' <= char <= 'z':
        return ord(char) - ord('a')
    elif 'A' <= char <= 'Z':
        return ord(char) - ord('A')
    else:
        raise ValueError("Ký tự không phải là chữ cái")
    

name = "nhnam"
x = maHoaTen(name, 26)
print("Mã hoá chuối `nhnam` ta được giá trị: ", x)
p1 = 6829
q1 = 7393
n1 = p1 * q1
a1 = 1564757
b1 = 10169981

p2 = 4051
q2 = 4567
n2 = p2 * q2
a2 = 1234567
b2 = 4648303
#x2 = 1619542
ver_recv = 28124669
sign_recv = 9257662
x_recv = modular_exponentiation(sign_recv, b1, n1)
print("Giá trị khi bản thân là phía gửi")
print("p = ", p1)
print("q = ", q1)
print("n = ", n1)
print("a = ", a1)
print("b = ", b1)
print(f"Bản mã khoá{n2, b2} gửi đi: ", modular_exponentiation(x, b2, n2))
print(f"Chữ kí{n1, a1} gửi đi: ", modular_exponentiation(x, a1, n1))
print("===========================================================")
print("Giá trị khi bản thân phía nhận")
print("p = ", p2)
print("q = ", q2)
print("n = ", n2)
print("b = ", b2)
print("Bản mã nhận được là: ", ver_recv)
print("Chữ kí nhận được là: ", sign_recv)
print("x cần tìm là: ", modular_exponentiation(sign_recv, b2, n2))
