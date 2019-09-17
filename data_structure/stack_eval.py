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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []

    for token in tokenList:
        if token == '(':
            opStack.push(token)
            continue
        if token == ')':
            while not opStack.isEmpty():
                last = opStack.pop()
                if last == '(':
                    break
                else:
                    postfixList.append(last)
        elif token in prec:
            if opStack.isEmpty():
                opStack.push(token)
            else:
                if prec[opStack.peek()] >= prec[token]:
                    postfixList.append(opStack.pop())
                opStack.push(token)
        else:
            postfixList.append(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return postfixList


def postfixEval(tokenList):
    opStack = ArrayStack()
    for token in tokenList:
        if type(token) == int:
            opStack.push(token)
        else:
            o2 = opStack.pop()
            o1 = opStack.pop()
            if token == "+":
                res = o1 + o2
            elif token == "-":
                res = o1 - o2
            elif token == "*":
                res = o1 * o2
            else:
                res = o1 / o2
            opStack.push(res)
    val = opStack.pop()
    return val

def solution(expr):
    
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val