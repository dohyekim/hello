class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''
    for x in S:
        if x == '(':
            opStack.push(x)
            continue
        if x in prec: # 연산자인 경우
            if opStack.isEmpty():
                opStack.push(x)
            else:
                if (prec[opStack.peek()] >= prec[x]):
                    answer += opStack.pop()
                opStack.push(x)
        elif x == ')': # )인 경우
            while not opStack.isEmpty():
                last = opStack.pop()
                if last != '(':
                    answer += last
                else:
                    break
        else: # 알파벳인 경우
            answer += x
        
    while not opStack.isEmpty():
        answer += opStack.pop()
        
        
    return answer