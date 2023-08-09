def max(list: list, current_max: int = 0) -> int:
    
    if list == []:
        return current_max
    
    if list[0] > current_max:
        return max(list[1:], list[0])
    else:
        return max(list[1:], current_max)
    

def max2(list:list):

    if len(list) == 1:
        return list[0]
    
    if list[0] > list[1]:
        list.pop(1)
    else:
        list.pop(0)
    return max2(list)


def max3(list:list):
    
    if len(list) == 1:
        return list[0]
    
    if list[0] > list[1]:
        list[1] = list[0]
    
    return(max3(list[1:]))


def max4(list):
    
    if len(list) == 2:
        if list[0] > list[1]:
            return list[0]
        else:
            return list[1]
    
    tmp = max4(list[1:])
    if list[0] > tmp:
        return list[0]
    else:
        return tmp


print(max4([10,200,0,10,910]))