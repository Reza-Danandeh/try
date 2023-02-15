def minimum(ls):
    min = ls[0]
    for number in ls:
        if min > number:
            min = number
    return min