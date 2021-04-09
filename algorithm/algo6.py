'''
자릿수의 합
N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 
그 합이 최대인 자연수를 출력 하는 프로그램을 작성하세요. 
각 자연수의 자릿수의 합을 구하는 함수를 
def digit_sum(x)를 꼭 작성해서 프로그래밍 하세요.
'''

#입력값
# 3
# 125 15232 97

import sys
sys.stdin=open('input.txt', 'r')
n=int(input())
a=list(map(int, input().split()))

# 각 자리수의 합 구하기
# 방법 1 : 각 자리숫자를 int화 시켜서 합 구하기
def digit_sum(x):
    sum=0
    for i in str(x):
        sum+=int(i)
    return sum

# 방법2 : 몫, 나머지를 이용하여 각 자리숫자의 합 구하기
def digit_sum(x):
    sum=0
    while x>0:
        sum+=x%10
        x=x//10
    return sum

max=-2147000000    
for x in a:
    total=digit_sum(x)
    if total>max:
        max=total
        res=x
print(res)