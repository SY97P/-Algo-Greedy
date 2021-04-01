'''

그리디 알고리즘

3 - 4. 1이 될 때까지

직관풀이

'''
def main() :
    n , k = map(int, input().split())

    count = 0
    
    while True :
        if n == 1 :
            break
        # n이 k로 나누어떨어진다면
        if n % k == 0 :
            n /= k
        else :
            n -= 1
        count += 1

    print(count)

main()
