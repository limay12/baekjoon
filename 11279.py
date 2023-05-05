import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1]) # (-x, x)에서 x 출력
    else:
        heapq.heappush(heap, (-x, x)) # min-heap 이기 때문에 max 정렬을 위해 -x 기준으로 정렬
