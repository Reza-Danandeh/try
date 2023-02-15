def maximum(ls):
    min = 0
    
    for number in ls:
        if number < min:
            min = number
    return min
