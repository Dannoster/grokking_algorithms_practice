def binary_search(list: list, answer: int):
    
    center_index = len(list)//2
    if list[center_index] == answer:
        return center_index
    elif len(list) == 1:
        return None
    elif list[center_index] > answer:
        return binary_search(list[:center_index], answer)
    elif list[center_index] < answer:
        try:    return center_index+1 + binary_search(list[center_index+1:], answer)
        except TypeError:   return None
    
print(binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 17))