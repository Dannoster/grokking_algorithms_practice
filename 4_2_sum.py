def sum(arr: list) -> int:
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum(arr[1:])

def simp_sum(list:list) -> int:
    total = 0
    for item in list:
        total += item
    return total

print(sum([2, 6, 4]))
print(simp_sum([2, 6, 4]))