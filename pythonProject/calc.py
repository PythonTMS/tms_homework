class Parser:
    def __init__(self, exp):
        self.exp = '(' + exp + ')'
        self.operands = []
        self.functions = []
        self.pos = 0
    #операторы и приоритет их выполнения (чем больше значение, тем меньше приоритет)
    operators = {'+': 2, '-': 2, '*': 1, '/': 1, '^': 0}

    #функция проверки операции(+, -, * и т.п.)
    @staticmethod
    def is_function(ch):
        return ch in Parser.operators.keys()

    #функция проверки приоритета операции
    @staticmethod
    def func_priority(ch):
        return Parser.operators[ch]

    #функция считывания числа
    def read_number(self):
        result = ''
        ch = self.exp[self.pos]

        while ch.isdigit() or ch == '.':
            result += ch
            self.pos += 1
            ch = self.exp[self.pos]
        return result

    #выполнение опрераций над операндами
    def execute_function(self):
        if len(self.operands) < 2:
            return

        a = self.operands.pop()
        b = self.operands.pop()
        f = self.functions.pop()

        if f == '+':
            self.operands.append(b + a)
        elif f == '-':
            self.operands.append(b - a)
        elif f == '*':
            self.operands.append(b * a)
        elif f == '/':
            self.operands.append(b / a)
        elif f == '^':
            self.operands.append(b ** a)

    #фомирование токена
    def get_token(self):
        for i in range(self.pos, len(self.exp)):
            ch = self.exp[i]
            if ch.isdigit():
                return self.read_number()
            else:
                self.pos += 1
                return ch
        return None


