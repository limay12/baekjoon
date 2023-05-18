import sys
input = sys.stdin.readline

# 서로소 집합 자료구조
# 특정 원소가 속한 집합을 찾기
def find_parent(x):
		# 경로 압축 기법
    # 루트 노드를 찾을 때까지 재귀 호출
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(a, b): # 신장 트리에 포함
    a = find_parent(a)
    b = find_parent(b)

    # 이미 부모가 같다면 리턴
    if a == b:
        return

    if rank[a] > rank[b]:
        parent[b] = a
    elif rank[a] < rank[b]:
        parent[a] = b
    else:
        parent[a] = b
        rank[b] += 1

N, M = map(int, input().split())
graph = []
parent = [i for i in range(N + 1)]  # 부모 테이블 자기 자신으로 초기화
rank = [0] * (N + 1)  # 각 노드마다 랭크를 저장
for i in range(M):
    a, b, cost = map(int, input().split())
    graph.append((cost, a, b))
        
graph.sort() # 비용순 정렬
ans = 0  # 연결된 마을 길이의 합
end_v = 0  # 마지막에 연결된 마을 길이를 저장

for i in graph:
		cost, a, b =  i
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        ans += i[0]  # 마을의 연결 비용들을 계속 더해주고
        end_v = i[0]  # 마지막에 연결된 마을 연결 비용을 저장

print(ans - end_v)  # 마지막에 연결된 연결 비용만 빼고 출력
