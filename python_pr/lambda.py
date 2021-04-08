'''
plus_two=lambda x: x+2
print(plus_two(1))
'''
def plus_one(x):
    return x+1

a=[1,2,3]
# map(함수명, 인자)
print(list(map(plus_one, a)))
# [2, 3, 4]

print(list(map(lambda x: x+1, a)))
# [2, 3, 4]
# 함수로 호출하는것이 아니라 바로 표현식으로 가능
