# Block 내에서 global keyword가 없을시 Local variable!!
# (별도의 메모리 공간에 위치)

g_x = 1000

def change_x():
    #global g_x
    g_x = 300
    print("inner def>>", g_x)

change_x()
print("222>>", g_x)

