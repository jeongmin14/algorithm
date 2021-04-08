# 공백없이 출력하기
# msg='It is Time'
# for x in msg:
#     if x.isalpha(): 
#         print(x, end='')
# print()

# tmp='AZ'
# for x in tmp:
#     print(ord(x)) 

'''
list(1)
'''

# import random as r
# a=list(range(1, 10))
# print(a)
# a.append(4) # 4 요소추가
# print(a)
# a.insert(3,19) #3번인덱스에 19 추가
# print(a)

# r.shuffle(a)
# print(a)
# a.sort() # 오름자순으로 정렬
# print(a) 
# a.sort(reverse=True) # 내림차순으로 정렬
# print(a)
# a.clear()
# print(a)

'''
list(2)
'''
a=[23,12,36,53,19]
print(a[:3]) #0번 인덱스에서 2번 인덱스까지 출력
print(a[1:4]) #1번 인덱스부터 3번 인덱스
print(len(a))

for x in a:
    print(x, end=' ')
print()

for x in a:
    if x%2==1:
        print(x, end=' ') #list요소중 홀수만 출력
print() 

for x in enumerate(a): #인덱스번호와 요소를 튜플형태로 출력
    print(x)
print()

for index, value in enumerate(a):
    print(index, value) #인덱스 번호와 리스트 요소를 함께 출력
print()

if all(53>x for x in a): #모두 참일 때 출력
    print("YES")
else:
    print("NO") #하나라도 거짓일경우 출력

if any(1>x for x in a): #하나라도 참일 때 출력
    print("YES")
else:
    print("NO") #모두가 거짓일경우 출력

