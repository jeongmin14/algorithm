'''
정다면체

두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확 률이 높은 숫자를 출력하는 프로그램을 작성하세요.
정답이 여러 개일 경우 오름차순으로 출력합니다.
N과 M은 4, 6, 8, 12, 20 중의 하나입니다.
'''
# 입력예제
# 4 6
import sys

sys.stdin=open('input.txt', 'r')
n, m=map(int, input().split())
cnt=[0]*(n+m+3)
max=0
print(cnt)
for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j]+=1

for i in range(n+m+1):
    if cnt[i]>max:
        max=cnt[i]
for i in range(n+m+1):
    if cnt[i]==max:
        print(i, end=' ')
