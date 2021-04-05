'''

백준 알고리즘

그리디 알고리즘

브론즈

컵홀더 문제

좌석 양 쪽에 컵홀더가 있는 일반 좌석과, 사이 공간에는 컵홀더가 없는 커플석이 있다.

총 n개의 좌석에 일반좌석과 커플석의 위치를 입력으로 받아서 

컵홀더에 컵을 넣을 수 있는 최대 사람의 수를 출력한다.


코로나 시대에서는 굳이 상상하지 않아도 될 문제긴 하다. 

9
*S*LL*LL*S*S*LL*

-> 2명이 못 씀(7명이 쓸 수 있음)

[1]S[2]L[x]L[3]L[x]L[4]S[5]S[6]L[x]L[7]

*LL*S*LL*LL*S*S* -> 7
[1]L[x]L[2]S[3]L[x]L[4]L[x]L[5]S[6]S[7]

*LL*S*LL*S*S*S*S* -> 8

*LL*S*LL*LL*LL* -> 6

*S*S*S*S*S*S*S*LL*

최대 좌석일 때는 모두 일반석일 때 n+1개
커플석이 두개 이상 생길 때마다 한 명씩 못 쓰는 사람이 생김.


'''
def main() :
	# 좌석 수
	num = int(input())
	
	# 일반 좌석과 커플석 배치를 문자열로 받음
	seat = input()
	
	count = 0
	
	for i in range(num) :
		#print(seat[i])
		# "L"이 두개 일 때 count를 하나 올림
		# count가 2 이상일 때부터 n+1 에서 count-1 을 제거
		if seat[i] == "L" :
			count += 1

	# "LL"의 개수
	count //= 2
	
	if count > 1 :
		print((num+1)-(count))
	else :
		print(num)

main()
