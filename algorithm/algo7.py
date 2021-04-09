'''
소수의 개수 출력(에라토스테네스 체)

자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요. 
만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다. 
제한시간은 1초입니다.
'''
# 입력값
# 20

import sys
sys.stdin=open('input.txt', 'r')
n=int(input())
a=[0]*(n+1)
cnt=0 # 소수의 개수
for i in range(2, n+1):
    if a[i]==0:
        cnt+=1
        for j in range(i,n+1,i): # i배수
            a[j]=1 #소수가 아닐 경우 요소가 1
print(cnt)

# leetcode 204_CountPrime
def countPrimes(n):
    if n<=2:
        return 0
    primes=[True]*n
    primes[0]=primes[1]=False
    for i in range(2, n):
        if primes[i]:
            for j in range(i*i, n, i):
                primes[j]=False
    return sum(primes)

print(countPrimes(2))