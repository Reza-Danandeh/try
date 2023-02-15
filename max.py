def maximum(ls):

    min = ls[0]

    for number in ls:
        if number < min:
            min = number
    return min
