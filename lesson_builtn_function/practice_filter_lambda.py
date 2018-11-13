int_numbers = range(-5, 6)
print(list(int_numbers))

negatives = filter(lambda x: x<0, int_numbers)
print(list(negatives))

print(negatives)

positive = filter(lambda x: x>0, int_numbers)
print(list(positive))

odd = filter(lambda x: x>0 and x % 2 == 1, int_numbers)
print(list(odd))

