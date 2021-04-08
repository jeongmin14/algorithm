# leetcode 125 
def isPalindrome(s):
    strs=[] # 빈 배열 세팅
    for i in s:
        if i.isalnum(): # 알파벳, 숫자 판별
            strs.append(i.lower()) # True일 경우 배열에 소문자로 바꾼 뒤 저장

    return strs == strs[::-1] # 기존배열과 뒤집었을때 배열 비교

s="A man, a plan, a canal: Panama"
print(isPalindrome(s))