import re
import ast

def compare_value(left, right):
    return left <= right

def left_is_empty_first(left, right, i):
    a = i == left - 1
    b = i < right - 1
    return a and b

def compare_list(left, right):
    left_len = len(left)
    right_len = len(right)
    ret_val = False
    for i, (left_value, right_value) in enumerate(zip(left, right)):
        if type(left_value) == int and type(right_value) == int:
            if left_value < right_value:
                ret_val = True
                break
            elif left_value == right_value:
                continue
            elif left_value > right_value:
                ret_val = False
                break
            elif left_is_empty_first(left_len, right_len, i):
                ret_val = True
                break
            else:
                ret_val = False
                break
        elif type(left_value) == list and type(right_value) == int:
            right_value = [right_value]
            ret_val = compare_list(left_value, right_value)
        elif type(left_value) == int and type(right_value) == list:
            left_value = [left_value]
            ret_val = compare_list(left_value, right_value)
        else:
            ret_val = compare_list(left_value, right_value)
    return ret_val


with open('./day-13/test') as f:
    alarm_codes = [line.rstrip('\n') for line in f.readlines()]
    parsed_code_pairs = []
    for i in range(0, len(alarm_codes) - 1, 3):
        left_code = []
        right_code = []
        if len(alarm_codes[i]) > 0:
            # print(ast.literal_eval(alarm_codes[i]))
            left_code.extend(ast.literal_eval(alarm_codes[i]))
            right_code.extend(ast.literal_eval(alarm_codes[i+1]))
            parsed_code_pairs.append([left_code, right_code])
        else:
            continue

cnt = 0
for i, pair in enumerate(parsed_code_pairs):
    if compare_list(pair[0], pair[1]):
        print(i+1)
        cnt += i+1

print(cnt)

#print(parsed_code_pairs)