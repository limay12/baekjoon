N, K = map(int, input().split())
coins = []

for _ in range(N):
	coins.append(int(input()))

coins.reverse()
answer = 0

for i in coins
	if i <= K:
		answer += K // i # i원 동전 개수
		K %= i # 나머지 금액
		if K == 0: 
			break

print(answer)
