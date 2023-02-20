import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 중복제거, 정렬
arr2 = list(sorted(set(arr)))
# { dic[좌표] : 좌표의 index }의 형태로 딕셔너리 저장
dic = {arr2[i] : i for i in range(len(arr2))}

for i in arr:
    print(dic[i], end=' ')
