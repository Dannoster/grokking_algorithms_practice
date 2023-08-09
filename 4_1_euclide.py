def find_max_square(a: int, b: int) -> int:
    a, b = max(a, b), min(a, b)
    if a % b == 0:
        return b
    else:
        new_a, new_b = a - b * (a // b), b
        return find_max_square(new_a, new_b)

print(find_max_square(1680, 640))