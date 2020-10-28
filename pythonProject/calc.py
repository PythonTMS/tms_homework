class Parser:
    def __init__(self, exp):
        self.exp = '(' + exp + ')'
        self.operands = []
        self.functions = []
        self.pos = 0
        self.prev_token = None
    # операторы и приоритет их выполнения (чем больше значение, тем меньше приоритет)
    operators = {'+': 2, '-': 2, '*': 1, '/': 1, '^': 0}

    # функция проверки операции(+, -, * и т.п.)
    @staticmethod
    def is_function(ch):
        return ch in Parser.operators.keys()

    # функция проверки приоритета операции
    @staticmethod
    def func_priority(ch):
        return Parser.operators[ch]

    # проверка на число с плавающей точкой
    @staticmethod
    def isfloat(num):
        try:
            float(num)
            return True
        except ValueError:
            return False

    # функция считывания числа
    def read_number(self):
        result = ''
        ch = self.exp[self.pos]

        while ch.isdigit() or ch == '.':
            result += ch
            self.pos += 1
            ch = self.exp[self.pos]
        return result

    # выполнение опрераций над операндами
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

    # фомирование токена
    def get_token(self):
        for i in range(self.pos, len(self.exp)):
            ch = self.exp[i]
            if ch.isdigit():
                return self.read_number()
            else:
                self.pos += 1
                return ch
        return None

    # сравнивание приоритетов операций
    def can_pop(self, ch):
        ch1 = self.functions[-1]
        if not Parser.is_function(ch1):
            return False
        p1 = self.func_priority(ch)
        p2 = self.func_priority(ch1)
        return p1 >= p2

    def calc(self):
        self.pos = 0
        token = self.get_token()

        while token:
            if token.isspace():
                pass
            elif token.isdigit():
                self.operands.append(int(token))
            elif self.isfloat(token):
                self.operands.append(float(token))
            elif Parser.is_function(token):
                while self.can_pop(token):
                    self.execute_function()
                self.functions.append(token)
            elif token == '(':
                self.functions.append(token)
            elif token == ')':
                while self.functions and self.functions[-1] != '(':
                    self.execute_function()
                self.functions.pop()
            self.prev_token = token
            token = self.get_token()
        return self.operands[0]


stroka = '2 + 4 * 2^2'
print(Parser(stroka).calc())