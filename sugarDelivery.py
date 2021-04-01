'''
백준 그리디 알고리즘

브론즈

설탕배달

'''
def main() :
    weight = int(input())

    count = 0
    while True :
        if weight % 5 == 0 :
            count += weight // 5
            break

        weight -= 3
        count += 1

        if weight < 0 :
            count = -1
            break
        
    print(count)

main()
