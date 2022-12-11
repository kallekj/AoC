import yaml
import numpy as np

debug = False


def printer(value: str):
    global debug
    if debug:
        print(value)


class Monkey:

    def __init__(self, index: int, starting_items: list, test_divisible: int, worry_level_modifier_value: str, worry_level_operator: str, throw_to_monkey_if_true: int, throw_to_monkey_if_false: int) -> None:
        self.index = index
        self.items = starting_items
        self.test_divisible = test_divisible
        self.worry_level_modifier_value = worry_level_modifier_value
        self.worry_level_operator = worry_level_operator
        self.throw_to_monkey_if_true = throw_to_monkey_if_true
        self.throw_to_monkey_if_false = throw_to_monkey_if_false
        self.inspected_items = 0
        self.worry_multiple = 0

    def set_worry_multiple(self, monkeys):
        self.worry_multiple = int(
            np.prod([monkey.test_divisible for monkey in monkeys]))

    def add_item(self, item: int):
        self.items.append(item)

    def inspect_next_item(self):
        def modifier_value_parser(modifier_value: str, item_value: int) -> int:
            if modifier_value == 'old':
                return item_value
            else:
                return int(modifier_value)
        self.inspected_items += 1
        item = self.items.pop(0)
        printer(f'Monkey inspects an item with a worry level of {item}.')
        match self.worry_level_operator:
            case '+':
                worry_level = item + \
                    modifier_value_parser(
                        self.worry_level_modifier_value, item)
                printer(
                    f'Worry level increases by {modifier_value_parser(self.worry_level_modifier_value, item)} to {worry_level}.')
            case '*':
                worry_level = item * \
                    modifier_value_parser(
                        self.worry_level_modifier_value, item)
                printer(
                    f'Worry level is multiplied by {modifier_value_parser(self.worry_level_modifier_value, item)} to {worry_level}.')
            case _:
                worry_level += 0

        worry_level %= self.worry_multiple
        printer(
            f'Monkey gets bored with item. Worry level is divided by 3 to {worry_level}')
        return worry_level

    def throw_next_item(self, item: int, monkeys: list):
        if item % self.test_divisible == 0:
            printer(
                f'Current worry level is divisible by {self.test_divisible}.')
            monkey: Monkey = monkeys[self.throw_to_monkey_if_true]
            printer(
                f'Item with worry level {item} is thrown to monkey {monkey.index}')
            monkey.add_item(item)
        else:
            printer(
                f'Current worry level is not divisible by {self.test_divisible}.')
            monkey: Monkey = monkeys[self.throw_to_monkey_if_false]
            printer(
                f'Item with worry level {item} is thrown to monkey {monkey.index}')
            monkey.add_item(item)

    def __str__(self) -> str:
        return f'Monkey {self.index}'


with open('./day-11/input') as f:
    try:
        instructions = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(e)

monkeys = []

for i, instruction in enumerate(instructions.values()):
    if type(instruction['Starting items']) == int:
        starting_items = [instruction['Starting items']]
    else:
        starting_items = [int(item)
                          for item in instruction['Starting items'].split(', ')]
    operation = instruction['Operation'].split(' ')[-2:]
    worry_level_operator = operation[0]
    worry_level_modifier_value = operation[1]
    divisible_by = int(instruction['Test'].split(' ')[-1])
    if_true = int(instruction['If true'].split(' ')[-1])
    if_false = int(instruction['If false'].split(' ')[-1])
    monkeys.append(Monkey(i, starting_items, divisible_by,
                   worry_level_modifier_value, worry_level_operator, if_true, if_false))

for monkey in monkeys:
    monkey.set_worry_multiple(monkeys)

for i in range(1, 10001):
    printer(f'Round {i} \n')
    for monkey in monkeys:
        printer(f'Monkey {monkey.index}:')
        for _ in range(len(monkey.items)):
            item = monkey.inspect_next_item()
            monkey.throw_next_item(item, monkeys)
            printer('\n')

    if i in [1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]:
        print(f'Round {i} \n')
        for monkey in monkeys:
            print(
                f'Monkey {monkey.index} inspected items {monkey.inspected_items} times.')
        print('\n\n')


for monkey in monkeys:
    print(
        f'Monkey {monkey.index} inspected items {monkey.inspected_items} times.')


def inspected_items(monkey: Monkey) -> int:
    return monkey.inspected_items


sorted_monkeys = sorted(monkeys, key=inspected_items)
print('============Solution============')
print(sorted_monkeys[-2].inspected_items * sorted_monkeys[-1].inspected_items)
