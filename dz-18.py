def common_elements():
    l1 = [num for num in range(1, 100) if num % 3 == 0]
    l2 = [num for num in range(1, 100) if num % 5 == 0]
    return print(set(l1).union(set(l2)))

common_elements()

