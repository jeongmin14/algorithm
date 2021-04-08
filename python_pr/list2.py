a=[0]*3
print(a)

# 2중배열
a=[[0]*3 for _ in range(3)] 
print(a)
a[0][1]=1
print(a)
a[1][1]=2
print(a)

# 2중배열을 3x3형식으로 출력
for x in a:
    print(x) 
print()

# 3x3형식으로 요소만 출력
for x in a:
    for y in x:
        print(y, end=' ')
    print()