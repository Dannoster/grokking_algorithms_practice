def count(list: list) -> int:
    if len(list) == 0:
        return 0
    return 1 + count(list[1:])
    
print(count([1,2,3,4,5,6,7]))