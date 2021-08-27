import hashlib

m = hashlib.md5()
m.update(b'123456')
print(m.hexdigest())
m.update(b'123')  # 实际算的b'123456123'
print(m.hexdigest())
m = hashlib.md5()  # 每次重新生成一个再算
m.update(b'123456123')
print(m.hexdigest())
print(m.digest())  # 有不可视字符
