from collections import deque
import numpy as np
import os
def clear(): return os.system('clear')


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
last_tick = 0
sprite = deque(['#']*3 + ['.']*37)
crt = []
currentRow = []
current_row_index = 0


def init() -> Instruction:
    global programQueue
    currentInstruction: Instruction = programQueue.pop(0)
    return currentInstruction


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
    clock.tick()
    firstSpriteIndex = sprite.index('#')
    steps_to_rotate = len(sprite) - firstSpriteIndex + regx.get_value() - 1
    sprite.rotate(steps_to_rotate)


def draw_pixel():
    global currentRow
    global current_row_index
    if len(currentRow) > 0:
        currentPixel = len(currentRow)
    else:
        currentPixel = 0

    def _add_pixel():
        pixelArr = np.array([False]*len(sprite))
        pixelArr[currentPixel] = True
        spriteArr = np.array([item == '#' for item in list(sprite)])
        marker = pixelArr & spriteArr
        if marker[currentPixel]:
            if len(currentRow) < 40:
                currentRow.append('#')
            else:
                currentRow[currentPixel] = '#'
        else:
            if len(currentRow) < 40:
                currentRow.append('.')
            else:
                currentRow[currentPixel] = '.'

    if currentPixel < 40:
        _add_pixel()
    else:
        crt.append(currentRow)
        currentRow = []
        current_row_index += 1
        currentPixel = 0
        _add_pixel()


def render_frame():
    if len(currentRow) == 40:  # Bugfix.. For some reason, the program finished before the last row is appended to the CRT
        crt.append(currentRow)
    for row in crt:
        print(row)


programQueue = read_program('./day-10/input')
currentInstruction = init()
while program_is_running:
    clock_generator()
    currentInstruction, last_tick = program_runner()
    draw_pixel()
    printer(regx)


render_frame()
