'''
반복문
'''
# for i in range(10, 0, -1): # 10부터 1씩 작아지도록
#     print(i)

# for i in range(1, 11):
#     if i%2==0:
#         continue #짝수일때는 넘어가고 홀수일 때 출력
#     print(i)

# for i in range(1, 11):
#     print(i)
#     if i==15:
#         break # break문으로 종료됐을 경우 else문 실행x
# else: #for문이 정상적으로 종료했을 경우 else문 실행
#     print(11)
'''
반복문을 이용한 문제풀이
'''
# # 1부터 n까지의 홀수 구하기
# n=int(input())
# for i in range(1, n+1):
#     if i%2==1:
#         print(i)

# # 1부터 n까지의 합 구하기
# n=int(input())
# sum=0
# for i in range(1, n+1):
#     sum=sum+i
# print(sum)

# # n의 약수 출력하기
# n=int(input())
# for i in range(1, n+1):
#     if n%i==0:
#         print(i, end=' ')

# # n의 약수 출력하기(list로 출력)
# n=int(input())
# aliquot_list=[]
# for i in range(1, n+1):
#     if n%i==0:
#         aliquot_list.append(i)
# print(aliquot_list)