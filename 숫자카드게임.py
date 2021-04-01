'''

그리디 알고리즘

3 - 3. 숫자 카드 게임

직관풀이

'''
def main() :
    n, m = map(int, input().split())

    minlst = []
    
    for i in range(n) :
        arr = list(map(int, input().split()))

        minlst.append(min(arr))

    result = max(minlst)

    #print(minlst)
    print(result)


main()
