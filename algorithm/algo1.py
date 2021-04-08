# n의 약수 중 k번째 수 출력하기
# 약수가 4개일 때 k에 5가 입력될 경우 -1출력
# 6 3이 입력되었을 경우(6의 약수는 1,2,3,6이므로) 3 출력
# 6 5가 입력되었을 경우 -1 출력

n, k = map(int, input().split())

cnt=0
for i in range(1,n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break
else:
    print(-1)