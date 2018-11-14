#Block 내에서 global keyword가 없을시 Local Variable!!
#(별도의 메모리 공간에 위치)

g_x = 1000
def change_x():
	# global g_x
	g_x = 300         # g_x = 1000과 다른 메모리에 있음. g_x = 1000은 전역변수, g_x=300은 지역변수, 이 때 global g_x를 쓰면 g_x=100과 g_x=300은 같은 전역변수가 된다.
	print("inner def>>", g_x)

change_x()
print("222>>", g_x)