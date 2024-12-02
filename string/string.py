
# 여러줄 문자열
print("""\
동해물과 백두산이
마르고 닳도록
하느님이 보우하사
우리나라 만세
무궁화 삼천리 화려강산
대한사람 대한으로
길이 보전하세\
""")
print('=========')

# 8_문자열 연산자
print("abc" + "abc")
print("abc" * 3)

# 문자열 선택 연산자(슬라이싱)
ex = "abcde"
print(ex[0]) # 인덱싱
print(ex[1:3]) # 2번째 ~ 3번째까지 -> bc / 슬라이싱

# 문자열[인덱스:인덱스:스탭]
ex = "0123456789"
print(ex[1:4:2])
print(ex[::3]) # 0369
print(ex[::-1]) # 스텝 -1 => 문자열 전체 뒤집기
print('===============문자열의 길이===============')
# 문자열의 길이
print(len('안녕하세요'))

print('===============format, split===============')
ex = "{} + {} = {}".format(10, 20, 10+20)
print(ex)
ex = "10-20-30-40".split("-")
print(ex)
ex = f"{10} + {20} = {10 + 20}"
print(ex)
ex = f"""\
{10} + {20} = {10 + 20}
{10} - {20} = {10 - 20}\
"""
print(ex)

# 정수 규격화
print("{:d}".format(52))
## 특정 칸만큼 출력
print("{:5d}".format(52))
print("{:10d}".format(52))
print("{:010d}".format(52)) # 0으로 패딩
print("{:5d}".format(52))
print("{:5d}".format(-52))
print("{:=+5d}".format(52))
print("{:=5d}".format(-52)) # 부호를 맨앞으로 붙여서 출력

# 실수
print("{:20.1f}".format(52)) # 소수점 이하 첫번쨰
print("{:20.2f}".format(52)) # 소수점 이하 두번쨰
print("{:20.3f}".format(52.2777)) # 소수점 이하 세번째까지, 4번째는 반올림

print('===============ex: 빗변 길이 구하기===============')
# a = input("밑변: ")
# a = float(a)

# b = input("높이: ")
# b = float(b)
# 피타고라스정리
# c = ((a**2) + (b**2)) **(1/2)
# print(f"빗변: {c}")

print('===============upper, lower===============')
a = "Hello python"
print(a.lower())
print(a.upper())

print('===============strip() : 공백제거 함수===============')
a = " 테스트  "
b = "abcd"
print(a.strip())
print(a.lstrip()) # 왼쪽 공백만 제거
print(a.rstrip()) # 오른쪽 공백만 제거

print(a.isalpha()) # 알파벳인지 체크
print(b.isalpha())

print('===============find(), rfind() : 문자열에서 문자가 어디에 존재하는지 확인===============')
# find() -> 왼쪽에서 부터 찾기
# rfind() -> 오른쪽에서 부터 찾기
a = "abcdabcd"
print(a.find("b")) # 1
print(a.rfind("b")) # 5
print(a.find("z")) # 못찾으면 -1

print('===============in 연산자===============')
print("안녕" in "안녕하세요") # True
print("hi" in "hhoi") # Fasle


