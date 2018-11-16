
# reduce(reduce_fn, iter) : one result

from functools import reduce

product = 1
lst = [1, 2, 3, 4]

for num in lst:
    product = product * num

print("product1>>", product)

product2 = reduce(lambda x, y: x * y, lst)
print("product2>>", product2)