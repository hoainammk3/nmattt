def modular_exponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus  # Chắc chắn rằng base nằm trong phạm vi modulo
    
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

# Sử dụng hàm để tính b^n mod m

# p = 10301, a = 3, b = 5, res = 10433
# p = 18181, a = 5, b = 5, res = 18251
# p = 827, a = 3, b = 5
# p = 827, a = 9, b = 7
p = 6828*7392
a = -1
b = 1564757
print(modular_exponentiation(b, a, p))
# mod_ar = []
# for i in range(1, (p+1)//2):
#     mod_ar.append(modular_exponentiation(i, 2, p))
# count = 0

# for i in range(0, p):
#     res = i*i*i + a*i + b
#     mod = modular_exponentiation(res, 1, p)
#     if (mod in mod_ar):
#         count = count + 2
#     if (50370 == i):
#         print("thoả mãn")