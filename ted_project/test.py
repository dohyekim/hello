
aa = []
class A:
    bb = []
    def qq(self):
        cc = 1
        self.bb.append(cc)
        # global aa
        aa.append(cc)


q = A()
q.qq()
print(aa)