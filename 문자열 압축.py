def solution(s):
    if len(s) == 1:
        return 1
    else:
        answer = []
        for i in range(1, (len(s) // 2) + 1):

            s_list = [s[0:i]]
            num_list = [1]

            for j in range(1, (len(s) // i)):
                if s_list[-1] != s[i * j:(j * i) + i]:
                    s_list.append(s[i * j:(i * j) + i])
                    num_list.append(1)

                else:

                    num_list[-1] += 1

            if len(s) % i != 0:
                s_list.append(s[-(len(s) % i) - 1:-1])

            cnt = 0
            for num in num_list:
                if num != 1:
                    cnt += ((num // 10) + 1)

            result = len(''.join(s_list)) + cnt
            answer.append(result)

        return min(answer)