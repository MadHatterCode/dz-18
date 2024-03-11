def common_elements():
    l1 = [num for num in range(1, 100) if num % 3 == 0]
    l2 = [num for num in range(1, 100) if num % 5 == 0]
    return set(l1).intersection(set(l2))


print(common_elements())

assert isinstance(common_elements(), set), "Test 1"
print("OK")
