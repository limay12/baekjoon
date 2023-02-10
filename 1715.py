import sys
import heapq

input = sys.stdin.readline

n = int(input())
cards = []
answer = 0
    
for i in range(n):
    cards.append(int(input()))

heapq.heapify(cards)

while len(cards) != 1 :
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    heapq.heappush(cards,a+b)
    answer += (a+b)

print(answer)
