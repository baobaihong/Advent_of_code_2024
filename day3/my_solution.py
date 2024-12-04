# Scan the corrupted memory for uncorrupted mul instructions and add them up to get the answer.

# part1
import re
with open('day3/input.txt', 'r') as file:
    corrupted_memory = file.read()
    # result = re.findall(r"mul\(\d+,\d+\)", corrupted_memory)
    # print(result)
    # answer = 0
    # for l,r in (result):
    #     answer += int(l)*int(r)
    
    # part2
    first_list = re.split(r'do\(\)', corrupted_memory)
    second_list = []
    final_list = []
    for string in first_list:
        split_list = re.split(r"don't\(\)", string)
        second_list.append(split_list[0])
    for string in second_list:
        final_list += re.findall(r"mul\((\d+),(\d+)\)", string)
    answer = 0
    for l,r in (final_list):
        answer += int(l)*int(r)
    print(answer)

    