int_numbers = range(-5, 6)
print(list(int_numbers))
# [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

negatives = filter(lambda x: x<0, int_numbers)
print(list(negatives))
# [-5, -4, -3, -2, -1]

print(negatives)
# <filter object at 0x000002D0CA6FBAC8>

positive = filter(lambda x: x>0, int_numbers)
print(list(positive))
# [1, 2, 3, 4, 5]

odd = filter(lambda x: x>0 and x % 2 == 1, int_numbers)
print(list(odd))
# [1, 3, 5]
