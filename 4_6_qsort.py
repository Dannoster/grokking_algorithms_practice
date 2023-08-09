# counter = 0

def qsort(list: list) -> list:
    # global counter

    if len(list) <= 1:
        return list
    
    center = len(list)//2
    llist = []
    rlist = []
    for i, item in enumerate(list):
        # counter += 1
        if i == center:
            continue
        elif item >= list[center]:
            rlist.append(item)
        else:
            llist.append(item)
    print(llist + [list[center]] + rlist)
    return(qsort(llist) + [list[center]] + qsort(rlist))
    
print(qsort([0,2,-1,15,0,6,64,3,19,-100,-100, 500,1,0,2,-1,15,0,6,64,3,19,-100,-100, 500,1]))
# print(counter)