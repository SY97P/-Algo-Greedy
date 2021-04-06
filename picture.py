'''
백준 알고리즘

DFS

실버

그림 문제


큰 도화지에 0은 여백, 1은 그림이라고 하자.

여러 그림 중에서 넓이가 가장 넓은 것의 넓이를 출력하자

피카소의 마음으로 풀어보자.

'''
def dfs(i, j, count) :
	print("i = ",i, ", j = ", j)
	# 해당하는 위치에 방문한 적도 없고, 그림도 그려져 있다면 진행시켜
	if visit[i][j] == 0 and screen[i][j] == 1 :
		visit[i][j] = 1
		count += 1
		print("max = ", max, ", count = ", count)
		global max
		print(max)
		
		# 오른쪽 먼저 확인해봄
		if visit[i][j+1] == 0 and screen[i][j+1] == 1 :
			dfs(i, j+1, count)
		# 그담에 아래쪽 확인해봄
		if visit[i+1][j] == 0 and screen[i+1][j] == 1 :
			dfs(i+1, j, count)
		# DFS니깐 다른 방향은 탐색하지 않아도 됨.

n, m = map(int, input().split())
	
# 도화지를 2차원 배열로 선언
screen = [[0 for j in range(m+1)] for i in range(n+1)]
# 탐색한 위치는 1로, 아닌 곳은 0으로
# 오른쪽 아래쪽 탐색할 때 out of index 걸리니까 한칸씩 더 크게 잡자(대신 1로 설정;가지마)
visit = [[0 for j in range(m+1)] for i in range(n+1)]

# 이제 입력으로 그림 그리자.
for i in range(n) :
	temp = list(map(int, input().split()))
	for j in range(m) :
		screen[i][j] = temp[j]
		
# 그림의 개수
count = 0

# 최대 넓이 그림
max = -1

for i in range(n) :
	for j in range(m) :
		dfs(i, j, count)
