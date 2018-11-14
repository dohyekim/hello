sort_students = sorted(students, key = lambda stu: stu.score)
print_students()
students.sort(key = lambda stu: stu.score)
print_students()
students.sort(key = lambda stu: stu.score, reverse=True)
print_students()
def sort_key(stu):
	return stu.score
students.sort(key = sort_key, reverse = True)
print_students()