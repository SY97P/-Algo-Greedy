'''
백준 알고리즘별 풀이

그리디 알고리즘

UCPC 문제

'''
def main() :
    line = input()

    ucpc = ["U", "C", "P", "C"]

    for i in range(len(line)) :
        if len(ucpc) == 0 :
            break
        #print(ucpc[0], line[i])
        if ucpc[0] == line[i] :
            del ucpc[0]
        
    

        
    if len(ucpc) == 0 :
        print("I love UCPC")
    else :
        print("I hate UCPC")
    


main()
