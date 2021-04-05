'''

백준 알고리즘

그리디 알고리즘

브론즈

세탁소 사장 동혁

사장 동혁이는 디아블로 게임, 알바생 리암은 똥멍청이.

나는 이 두 짐덩어리를 위해서 거스름돈 코딩을 해줘야 한다. 

$5.00 이하의 거스름돈을 쿼터($0.25), 다임($0.10), 니켈($0.05), 페니($0.01)로 
최소가 될 수 있도록 만들어보자.

동혁이와 리암이를 위해서

'''
def main() :
	# 테스트 케이스 개수
	case = int(input())
	
	# 각 테스트 케이스에서의 거스름 돈
	change = []
	for i in range(case) :
		change.append(int(input()))
	
	# 거슬러줄 수 있는 동전의 가치
	qu = 25
	di = 10
	ni = 5
	pe = 1
	

	
	'''
	for i in range(case) :
		print(change[i], end = " ")
	'''
	
	# 이제 본격적으로 돈을 거슬러주자.
	for i in range(case) :
		# 현재 거슬러줘야 하는 총액
		now = change[i]
		
		# 동전이 사용된 개수
		countQu, countDi, countNi, countPe = 0, 0, 0, 0
		
		# print(now)
		
		while now >= qu :
			now -= qu
			countQu += 1
		while now >= di :
			now -= di
			countDi += 1
		while now >= ni :
			now -= ni
			countNi += 1
		while now >= pe :
			now -= pe
			countPe += 1
		
		print(countQu, countDi, countNi, countPe)
	
main()
