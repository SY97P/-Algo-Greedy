'''
3-2 큰 수의 법칙

좀 더 나은 풀이

'''
def main() :

    n, m, k = map(int, input().split())

    arr = list(map(int, input().split()))

    arr.sort()
    first = arr[n-1]
    second = arr[n-2]

    # first 를 더해야하는 횟수
    count = int(m / (k+1)) * k
    count += m % (k+1)

    # 결과값
    result = count * first
    result += (m - count) * second

    print(result)


main()
