'''

백준 알고리즘

그리디 알고리즘

브론즈

전자레인지

요리시간 T초가 주어졌을 때 
A, B, C 세 버튼 (각각 5m, 1m, 10s)으로 요리할 수 있는가

불가능하면 -1 출력
가능하면 각 버튼당 누른 횟수 출력

'''
def main() :
	time = int(input())
	
	buttonA = 300
	buttonB = 60
	buttonC = 10
	
	countA, countB, countC = 0, 0, 0
	
	
	while time >= buttonA :
		countA += 1
		time -= buttonA
	while time >= buttonB :
		countB += 1
		time -= buttonB
	while time >= buttonC :
		countC += 1
		time -= buttonC
	if time != 0 :
		print(-1)
	else :
		print(countA, countB, countC)

	
main()
