def solution(sequence):
    flag = 0
    previous_element = sequence[0]
    for i in range(1, len(sequence)):
        if flag == 0:
            if previous_element < sequence[i]:
                previous_element = sequence[i]
                pass
            else:
                flag += 1
                pass
        if flag == 1:
            if previous_element < sequence[i]:
                pass
            else:
                flag += 1
                break
        else:
            break
    print(flag)
    if flag > 1:
        return False
    else:
        return True


solution([1, 3, 2, 1])
