def solution(s):
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for n in range(len(numbers)):
        s = s.replace(numbers[n], str(n))

    answer = int(s)

    # result = []
    #     s = list(s)

    #     while len(s) != 0:
    #         i = 0
    #         if s[i].isdecimal():
    #             result.append(int(s[i]))
    #             del s[i]

    #         else:
    #             for n in range(len(numbers)):
    #                 if s[i:i+2] == list(numbers[n][0:2]):
    #                     result.append(n)
    #                     del s[i:i+len(numbers[n])]
    #                     break

    #         answer = int(''.join(map(str,result)))

    return answer