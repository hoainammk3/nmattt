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
    
name = "AiYeuBacHoChiMinhNhuThieuNienNhiDong"
res = maHoaTen(name, 26)
print(res)