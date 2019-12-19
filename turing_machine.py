# coding:utf8
# author: Yixiao Lan
class Memory(object):
    def __init__(self, length):
        self.space = [None for _ in range(length)]
        self.length = length

    def malloc(self):
        for idx in range(self.length):
            if self.space[idx] is None:
                return idx
        raise Exception('MemoryError', 'Out if space.')

    def set_memory(self, addr, value):
        if addr >= self.length:
            raise Exception('MemoryError', 'Address > Memory max address.')
        self.space[addr] = value
        return

    def clear_memory(self, addr):
        if addr >= self.length:
            raise Exception('MemoryError', 'Address > Memory max address.')
        self.space[addr] = None
        return

    def read_memory(self, addr):
        if addr >= self.length:
            raise Exception('MemoryError', 'Address > Memory max address.')
        return self.space[addr]


class Controller(object):
    def __init__(self):
        self.cursor = 0
        self.input_sequence = None
        self.memory = Memory(length=1000)
        self.arithmetic_logic_unit = ArithmeticLogicUnit(self.memory)

    def set_operates(self, operation_sequence_input):
        self.input_sequence = operation_sequence_input
        return

    @staticmethod
    def turn_operation_into_tuple(operation):
        opt_arg = operation.split(' ')
        if len(opt_arg) == 1:
            return opt_arg
        args = opt_arg[1].split(',')
        return opt_arg[0], args

    def run(self):
        while True:
            operation = self.input_sequence[self.cursor]
            operation_tuple = self.turn_operation_into_tuple(operation)
            self.cursor = self.arithmetic_logic_unit.operate(operation_tuple, self.cursor)
            if self.cursor == -1:
                break
        # self.watch_memory()

    def watch_memory(self):
        print('Memory state is as follow:\n{}'.format(self.memory.space))


class ArithmeticLogicUnit(object):
    def __init__(self, bond_memory):
        self.bond_memory = bond_memory

    def detect(self, value):
        if str(value)[0] == '@':
            return self.bond_memory.read_memory(int(str(value)[1:])) if self.bond_memory.read_memory(int(str(value)[1:])) else 0
        return int(value)

    @staticmethod
    def get_cursor(value):
        if str(value)[0] != '@':
            return int(value)
        return int(str(value)[1:])

    def watch_memory(self):
        print('Memory state is as follow:\n{}'.format(self.bond_memory.space))

    def operate(self, operation_tuple, pc):
        opt = operation_tuple[0]
        if len(operation_tuple) != 1:
            args = operation_tuple[1]
        if opt == 'MOV':
            self.bond_memory.set_memory(addr=self.get_cursor(args[0]), value=self.detect(args[1]))
            return pc + 1
        if opt == 'ADD':
            register = self.detect(args[0])
            if not register:
                register = 0
            register += self.detect(args[1])
            self.bond_memory.set_memory(addr=self.get_cursor(args[0]), value=register)
            return pc + 1
        if opt == 'DEC':
            register = self.detect(args[0])
            if not register:
                register = 0
            register -= self.detect(args[1])
            self.bond_memory.set_memory(addr=self.get_cursor(args[0]), value=register)
            return pc + 1
        if opt == 'MUL':
            register = self.detect(args[0])
            if not register:
                register = 0
            register *= self.detect(args[1])
            self.bond_memory.set_memory(addr=self.get_cursor(args[0]), value=register)
            return pc + 1
        if opt == 'DIV':
            register = self.detect(args[0])
            if not register:
                register = 0
            register /= self.detect(args[1])
            self.bond_memory.set_memory(addr=args[0], value=register)
            return pc + 1
        if opt == 'EQU':
            if self.detect(args[0]) == self.detect(args[1]):
                return self.get_cursor(args[3])
            return pc + 1
        if opt == 'NEQ':
            if self.detect(args[0]) != self.detect(args[1]):
                return self.get_cursor(args[3])
            return pc + 1
        if opt == 'BGT':
            if self.detect(args[0]) >= self.detect(args[1]):
                return int(args[3])
            return pc + 1
        if opt == 'SMT':
            if self.detect(args[0]) <= self.detect(args[1]):
                return int(args[3])
            return pc + 1
        if opt == 'ANB':
            if self.detect(args[0]) and self.detect(args[1]):
                return int(args[3])
            return pc + 1
        if opt == 'ORB':
            if self.detect(args[0]) or self.detect(args[1]):
                return int(args[3])
            return pc + 1
        if opt == 'JMP':
            return int(args[0])
        if opt == 'END':
            return -1
        if opt == 'DEL':
            self.bond_memory.clear_memory(addr=self.get_cursor(args[0]))
            return pc + 1
        if opt == 'MLC':
            pass
            return pc + 1
        if opt == 'VAR':
            pass
            return pc + 1
        if opt == 'PRT':
            print(self.detect(args[0]))
            return pc + 1
        if opt == 'PRTM':
            self.watch_memory()
            return pc + 1
        raise Exception('Syntax Error', 'No such opt code : {}'.format(opt))


def parser(seq, spl=';'):
    seq = seq.replace('\n', '')
    return seq.split(spl)


if __name__ == '__main__':
    with open('tape.trl', 'r') as f:
        content = f.read()
    parsed_content = parser(content)
    controller = Controller()
    controller.set_operates(parsed_content)
    controller.run()





