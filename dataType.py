# print(5)
# print(-10)
# print(3.14)
# print(5+3)
# print(2*4)
# print("z"*9)
# print(5 < 10)
# print(5 > 10)
# print(True)
# print(False)
# print(not True)
# print(not False)

name = "Willy"
age = 30

print("My name is " + name + ".")
print(name + " is so smart,")
print("and has a great attitude.")
print(name + " is " + str(age) + " years old,")
print("but he looks like 23.")

station = "사당"
arriving_msg = "행 열차가 들어오고 있습니다."
print(station + arriving_msg)
station = "신도림"
print(station + arriving_msg)
station = "인천공항"
print(station + arriving_msg)

print((3 > 0) and (2 > 3))
print((3 > 0) & (2 > 3))

print((3 > 0) or (2 > 3))
print((3 > 0) | (2 > 3))

print(2 + 3 * 4)
print((2 + 3) * 4)

print(abs(-5))
print(pow(4, 2))

from math import *
print(floor(3.99))
print(ceil(3.14))
print(sqrt(16))

from random import *
# print(int(random() * 10))
# print(int(random() * 10))
# print(int(random() * 10))
# print(int(random() * 10))
# print(int(random() * 10) + 1)
# print(int(random() * 10) + 1)
# print(int(random() * 10) + 1)
# print(int(random() * 10) + 1)

# print(randrange(1, 46))
# print(randrange(1, 46))
# print(randrange(1, 46))
# print(randrange(1, 46))
# print(randrange(1, 46))

print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))

onlineDay1 = randint(4, 28)
onlineDay2 = randint(4, 28)
onlineDay3 = randint(4, 28)
offlineDay = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(offlineDay) + " 일로 선정되었습니다.")

sentence = "I'm a boy."
sentence2 = "Python is easy."
sentence3 = """I'm a boy,
and python is easy."""

print(sentence)
print(sentence2)
print(sentence3)