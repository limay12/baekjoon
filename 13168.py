import sys
from math import inf
input = sys.stdin.readline

N, R = map(int, input().split())
cities = set(input().split())
N = len(cities)
city_dic = {cities: i for i, cities in enumerate(cities)}
M = int(input())
travel = list(map(lambda x: city_dic[x], input().split()))

yes_ticket = [[inf] * N for _ in range(N)] # 티켓 있는 경로
no_ticket = [[inf] * N for _ in range(N)] # 티켓 없는 경로

for _ in range(int(input())):
    t, s, e, c = input().split()
    s = city_dic[s]
    e = city_dic[e]
    c = int(c)
    if no_ticket[s][e] > c:
        no_ticket[s][e] = c
        no_ticket[e][s] = c
    if t in ['Mugunghwa', 'ITX-Saemaeul', 'ITX-Cheongchun']:
        yes_ticket[s][e] = 0
        yes_ticket[e][s] = 0
    elif t in ['S-Train', 'V-Train']:
        if yes_ticket[s][e] > c / 2:
            yes_ticket[s][e] = c / 2
            yes_ticket[e][s] = c / 2
    else:
        if yes_ticket[s][e] > c:
            yes_ticket[s][e] = c
            yes_ticket[e][s] = c

# 플로이드-워셜
for k in range(N):
    yes_ticket[k][k] = 0
    no_ticket[k][k] = 0
    for i in range(N):
        for j in range(N):
            yes_ticket[i][j] = min(yes_ticket[i][j], yes_ticket[i][k] + yes_ticket[k][j])
            no_ticket[i][j] = min(no_ticket[i][j], no_ticket[i][k] + no_ticket[k][j])

# 티켓 유무에 따른 여행 총 가격 계산
no_cost = 0
yes_cost = 0
for i in range(M - 1):
    no_cost += no_ticket[travel[i]][travel[i + 1]]
    yes_cost += yes_ticket[travel[i]][travel[i + 1]]
    
if yes_cost + R < no_cost:
    print('Yes') 
else:
    print('No')
