import random
fam_names = list("김이박최강고윤엄한배성백전황서천방지마피")
first_names = list("건성현욱정민현주희진영래주동혜도모영진선재현호시우인성마무병별솔하라")
#insert into Student(name) values(?)
#executemany 쓰세요!!


def make_name():
    last_name = []
    last_name.append(random.choice(fam_names))

    name = random.sample(first_names, k = 2)

    full_name = last_name + name
    print(''.join(full_name))

make_name()