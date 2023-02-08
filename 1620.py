import sys
input = sys.stdin.readline

n,m = map(int, input().split())
dict = {}

# 딕셔너리로 도감 완성
for i in range(1, n+1):
    a = input().rstrip()
    dict[i] = a
    dict[a] = i
    
# 시험 풀기
for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(dict[int(quest)])
    else:
        print(dict[quest])
