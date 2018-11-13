# sorted(), reversed()

numbers = [5,3,4,2,1]

#sorted라는 내장함수 -> list 혹은 string을 순서대로 1,2,3,4,5로 정리해준다.
sort_numbers = sorted(numbers)     # cf. reversed(numbers): 내림차순

print("sort_numbers=", sort_numbers) #>>> sort_numbers= [1, 2, 3, 4, 5]
print("numbers=", numbers) #>>>numbers= [5, 3, 4, 2, 1]

numbers.sort()        #list도 sort함수를 갖고 있다.
print("asc>>", numbers) #>>> asc>> [1, 2, 3, 4, 5]

numbers.sort(reverse=True)  #list가 가진 sort함수에서 내림차순으로 하려면 (reverse=True)값을 줘야한다.
print("desc>>", numbers) #>>> desc>> [5, 4, 3, 2, 1]


# str

strs = ['aaaa', 'bbbb', 'ccc', 'dddd']
sort_strings = sorted(strs)

print("sort_strigns=", sort_strings)

strs.sort()
print("asc>>", strs)

strs.sort(reverse=True)
print("desc>>", strs)

t = (1,5,4)
print("000>>",sorted(t))

#t.sort()는 불가, 왜냐하면 tuple은 read only이기 때문. .sort()하게 되면 data를 전부 뒤집어서 다시 정렬하는 과정을 거침.