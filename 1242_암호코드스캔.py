import sys
sys.stdin = open('input.txt')

password = ['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']
T = int(input())
for t in range(T):
    N , M = map(int,input().split())
    arr = list(set(input().strip().strip('0') for _ in range(N)))
    new_arr=[]



    for a in arr:
        if '0000' in a:
            new_arr+a.split('000000')
        else:
            new_arr.append(a)


    for a in new_arr:
        if a == '':
            new_arr.remove(a)
    print(new_arr)
    print(len(new_arr))

    total_result=[]
    for num in range(len(new_arr)):
        result=[]
        new_arr[num] = '0000000000000000' + format(int(new_arr[num],16),'b')

        for i in range(len(new_arr[num])-1,-1,-1):
            if new_arr[num][i] == '1':
                idx = i
                break

        term = (len(new_arr[num])-16)//50

        for _ in range(8):
            result.append(new_arr[num][idx-(6*term):idx+1:term])
            idx-= 7*term

        result.reverse()
        total_result.append(result)


    answer= 0

    for result in total_result:
        pw = []
        for r in result:
            for p in range(10):
                if r==password[p]:
                    pw.append(p)




        if ((pw[0]+pw[2]+pw[4]+pw[6])*3 + (pw[1]+pw[3]+pw[5]) + pw[7]) % 10 == 0:
            answer+=sum(pw)
        else:
            answer+=0

    print(answer)
