a = 10 < 20 < 30

print(a) # True

x = 900
b = 10 < x <550 # False
print(b)
print(not b) # True
print()

a = "1020".isalnum() # 문자열이 영어, 한글 혹은 숫자로 되어있으면 참 리턴, 아니면 거짓 리턴.
print(a)
print()

# 이항연산

a = True or True # True
b = True or False # True
c = True and False # false
d = False and False # false
print(a, b, c, d) # True True False False

