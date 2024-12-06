## PART1: specify page arrays in the correct order and calculate the sum of middle number for each array
#1. the upper part of the string(format: X|Y) defines the rules of order for specific page, meaning index of X must be less than Y.(not necessarily next to each other)
#2. the middle number is the number positioned at the middle of the array.

file_path = 'day5/input.txt'

def separator(file: str):
    with open (file, 'r') as file:
        full_text = file.read().split('\n\n')
        rule_text = full_text[0]
        page_text = full_text[1]
        order_list = [[int(i) for i in line.split('|')] for line in rule_text.split('\n')]
        page_list = [[int(i) for i in line.split(',')] for line in page_text.split('\n')]
        return order_list, page_list
    
    
def page_judger(page1: int, page2: int, order_list: list):
    if [page1, page2] in order_list:
        return True
    else:
        return False
    
def middle_page_finder(page_array: list):
    length = len(page_array)
    return page_array[int((length - 1) / 2)]
    
order_list, page_list = separator(file_path)

middle_page_sum = 0
# for page_array in page_list:
#     array_length = len(page_array)
#     correct_array = True
#     for i in range(array_length - 1):
#         first_page = page_array[i]
#         for j in range(i + 1, array_length):
#             second_page = page_array[j]
#             if not page_judger(first_page, second_page, order_list):
#                 correct_array = False
#                 print(f"Wrong update: {page_array}, wrong order:[{first_page}|{second_page}].")
#                 break
#             else:
#                 continue
#         if not correct_array:
#             break
#     if correct_array:
#         middle_page_sum += middle_page_finder(page_array)
#         print(f"Correct update: {page_array}")

# print(f"The sum of middle page for correct updates is {middle_page_sum}")

## PART2: 
def update_judger(update: list[int]) -> tuple[bool, int, int]:
    update_length = len(update)
    for i in range(update_length - 1):
        first_page = update[i]
        for j in range(i + 1, update_length):
            second_page = update[j]
            if page_judger(first_page, second_page, order_list):
                continue
            else:
                return False, i, j
    return True, None, None

def update_modifier(update: list[int], first_index: int, second_index: int) -> list[int]:
    update_copy = update.copy()
    second_page = update[second_index]
    update_copy.pop(second_index)
    update_copy.insert(first_index, second_page)
    return update_copy

def update_correct_loop(update: list[int], first_index: int, second_index: int) -> tuple[dict]:
    iteration_history = {}
    iteration_history[0] = update
    correct, first_index_v1, second_index_v1 = update_judger(update)
    if correct:
        return iteration_history
    else:
        incorrect = True
        iteration_round = 1
        index_1 = first_index_v1
        index_2 = second_index_v1
        array = update
        while incorrect:
            # modify the update array
            array = update_modifier(array, index_1, index_2)
            # append to history
            iteration_history[iteration_round] = array
            # judge the update array agin
            result, first_index_v2, second_index_v2 = update_judger(array)
            if result == True:
                return iteration_history
            elif result == False:
                iteration_round += 1
                index_1 = first_index_v2
                index_2 = second_index_v2
            if iteration_round > 50:
                raise AssertionError(f"Too many times of iteration, {iteration_history}")
            

for update in page_list:
    correct, first_index, second_index = update_judger(update)
    if not correct:
        history = update_correct_loop(update, first_index, second_index)
        final_correct_udpate = list(history.values())[-1]
        middle_page_sum += middle_page_finder(final_correct_udpate)
    elif correct:
        pass

print(f"After correct every incorrect updates, the sum of middle page is {middle_page_sum}.")