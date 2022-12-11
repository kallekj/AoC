

class Register:

    def __init__(self) -> None:
        self.value = 1
        self.updated = True

    def get_value(self):
        return self.value

    def add_value(self, value) -> None:
        self.value += value
        self.updated = True
    
    def is_reading(self) -> None:
        self.updated = False 

    def has_updated(self) -> bool:
        return self.updated

    def __str__(self) -> str:
        return f'Register has value: {self.value}'


class Instruction():

    def __init__(self, cycles: int, instruction_name: str, action: int = 0) -> None:
        self.cycles = cycles
        self.instruction_name = instruction_name
        self.action = action

    def get_action(self) -> int:
        return self.action

    def get_cycles(self) -> int:
        return self.cycles

    def __str__(self) -> str:
        return f'{self.instruction_name} {self.action}'


class Clock:

    def __init__(self) -> None:
        self.counter = 0


    def tick(self) -> None:
        self.counter += 1

    def get_tick(self) -> int:
        return self.counter


def read_program(file_name: str) -> list:
    instructions = []
    with open(file_name) as f:
        program = [line.rstrip('\n') for line in f.readlines()]

    for instruction in program:
        if instruction == 'noop':
            instructions.append(Instruction(1, instruction))
        else:
            instruction, value = instruction.split(' ')
            value = int(value)
            instructions.append(Instruction(2, instruction, value))
    return instructions



def printer(value: str):
    global debug
    if debug:
        print(value)


# Variables
programQueue = []
currentInstruction: Instruction = None
regx = Register()
clock = Clock()
debug = False
program_is_running = True
last_tick = 2
signal = []

def init() -> Instruction:
    global programQueue
    currentInstruction: Instruction = programQueue.pop(0)
    regx.add_value(currentInstruction.get_action())
    printer(f'Instruction: {currentInstruction} is complete.') 
    nextInstruction: Instruction = programQueue.pop(0)
    printer(f'Reading instruction: {nextInstruction}')
    return nextInstruction
 

def program_runner() -> tuple((Instruction, int)):
    global regx
    global clock
    global program_is_running
    global currentInstruction

    if clock.get_tick() - last_tick >= currentInstruction.get_cycles():
        regx.add_value(currentInstruction.get_action())
        printer(f'Instruction: {currentInstruction} is complete.')
        if len(programQueue) == 0:
            program_is_running = False
            return (currentInstruction, clock.get_tick())
        else:
            nextInstruction: Instruction = programQueue.pop(0)
            printer(f'Reading instruction: {nextInstruction}')
            return (nextInstruction, clock.get_tick())
    else:
        return (currentInstruction, last_tick)


def clock_generator():
    global clock
    global regx
    clock.tick()
    if clock.get_tick() in [20, 60, 100, 140, 180, 220]:
        temp = regx.get_value()*clock.get_tick()
        signal.append(temp)
        printer(temp)
        printer(regx)


programQueue = read_program('./day-10/input')
currentInstruction = init()
while program_is_running:
    clock_generator()
    currentInstruction, last_tick =  program_runner()
    printer(regx)


print('Exit program')
print(f'Signal strength is: {sum(signal)}')

