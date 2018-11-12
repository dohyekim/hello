
class Square:
    
    def __init__(self):
        self.name = Square
    
    def multiply(self, a, b):
        return a * b

    def square_input(self):
        cmd = input("밑변, 높이")
        
        if cmd == "quit":
            break

        cmds = cmd.split(',')
        c = int(cmds[0])
        d = int(cmds[1])

    def msg(self):

        msg = "답은 {}이다."

        return msg.format(multiply(self, c, d)


paral = Square()

paral.square_input()





        
