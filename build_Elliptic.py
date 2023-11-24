from Crypto.PublicKey import ECC

# Chọn trường hữu hạn p
p_hex = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF7FFFFFFF"

# Chọn các hệ số a và b
a = -3
b_hex = "64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1"

# Chọn điểm cơ sở
x_hex = "188da80eb03090f67cbf20eb43a18800f4ff0afd82ff1012"
y_hex = "07192b95ffc8da78631011ed6b24cdd573f977a11e794811"

# Khởi tạo đường cong elliptic
curve = ECC._Curve(
    "my_curve",
    a = a,
    b = int(b_hex, 16),
    field = ECC.FiniteField(int(p_hex, 16)),
    generator = (int(x_hex, 16), int(y_hex, 16)),
    order = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141,
    oid = "1.2.840.10045.3.1.7",
)

# In thông tin về đường cong elliptic
print("Đường cong elliptic đã được khởi tạo:")
print("Tên đường cong:", curve.name)
