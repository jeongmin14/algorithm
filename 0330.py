# list정렬
a = [1, 10, 5, 7, 6]
a.reverse() # 리스트를 뒤집어서 출력
print(a)

a = [1, 10, 5, 7, 6]
a.sort() # 오름차순으로 정렬 
a.sort(reverse=True) # reverse=True일 경우 내림차순
print(a)
 
a = [1, 10, 5, 7, 6]
b =reversed(a) # 거꾸로 뒤집기
print(a) # [1, 10, 5, 7, 6]
print(b) # iterable한 객체를 반환, <list_reverseiterator object at 0x7fb1d4865130>
print(list(b))# list로 한번 더 변형 해줘야함, [6, 7, 5, 10, 1]

a = [1, 10, 5, 7, 6]
b = sorted(a)
print(a)
print(b)

# % 와format
print('%s %d개는 %.2f달러' %('사과', 3, 1.5))
%s에는 문자열, %d에는 정수, %f에는 실수(단, 디폴트 소수점6자리)
%.2f -> 소수점 두번째까지 출력하겠다...

print('{}, {}중에서 어느 것이 더 재밌나요?'.format('python', 'java')) 
# {}순서에 따라 연결된 단어가 출력됨, python, java중에서 어느 것이 더 재밌나요?

print('{1}, {0}중에서 어느 것이 더 재밌나요?'.format('python', 'java')) 
#{}안의 인덱스번호따라 배치, java, python중에서 어느 것이 더 재밌나요?