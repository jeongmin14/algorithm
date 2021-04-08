# 최솟값구하기

# arr=[5,3,7,9,2,5,2,6]
# arrMin=float('inf')
# for x in arr:
#     if x < arrMin:
#         arrMin=x
# print(arrMin)

# for i in range(len(arr)):
#     if arr[i]<arrMin:
#         arrMin=arr[i]
# print(arrMin)

'''
대표값

N명의 학생의 수학점수가 주어집니다. 
N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고, 
N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세요.
평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고, 
높은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.
'''
import sys

sys.stdin=open('input.txt', 'r')
n=int(input())
a=list(map(int, input().split()))

# n=10 
# a=45 73 66 87 92 67 75 79 75 80

ave=sum(a)/n
ave=int(ave+0.5)

#ave=round(sum(a)/n)
# round() : 입력받은 인자를 반올림하는 함수
# 두번째인자를 받으면 받은 숫자까지 소수점 표시
# round(3.1415, 2) 출력결과:3.14
# $주의$ round(4.5000)일 경우 4를 출력함, round_half_even 방식

min=2147000000
for idx, x in enumerate(a): #학생번호, 점수 출력
    tmp=abs(x-ave) #abs():절대값구하기, |점수와 평균의 차| 출력
    if tmp<min: #세팅해놓은 최소값보다 절대값이 작을경우
        min=tmp #절대값이 최소값이 된다
        score=x 
        res=idx+1
    elif tmp==min: #절대값과 최소값이 같은 경우
        if x>score: #새로들어온?점수가 기존에 저장된 점수보다 클 경우 
            score=x #바꿔준다...
            res=idx+1
print(ave, res)
