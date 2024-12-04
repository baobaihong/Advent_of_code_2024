## challenge 1: To find out, pair up the numbers and measure how far apart they are. 
## Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on.

## Reorder the list
def reorder_list(list):
    new_list = []
    length = len(list)
    for i in range(0, length):
        new_list = insert_num(new_list, list[i])
    return new_list

## Insert the number into the list in the correct position
def insert_num(list, num):
    if len(list) == 0:
        list.append(num)
    else:
        for i in range(0, len(list)):
            if num >= list[i]:
                if i == len(list) - 1:
                    list.append(num)
                else:
                    continue
            else:
                list.insert(i, num)
                break
    return list

def calculate_distance(left_column, right_column):
    distance = 0
    reordered_left = reorder_list(left_column)
    reordered_right = reorder_list(right_column)
    for i in range(0, len(left_column)):
        distance += abs(reordered_left[i] - reordered_right[i])
    return distance

## Import input data
# Open the file in read mode
with open('day1/input.txt', 'r') as file:
    # Initialize two empty lists
    left_column = []
    right_column = []
    
    # Iterate over each line in the file
    for line in file:
        # Split the line into two parts based on whitespace
        left, right = line.split()
        
        # Append the values to the respective lists
        left_column.append(int(left))
        right_column.append(int(right))

# Print the lists to verify
print("Left Column:", len(left_column))
print("Right Column:", len(right_column))

# Calculate the answer
print(calculate_distance(left_column, right_column))

## part2
def calculate_similarity_score(left_column, right_column):
    similarity_score = 0
    for i in range(0, len(left_column)):
        similarity_score += left_column[i] * right_column.count(left_column[i])
    return similarity_score

print(calculate_similarity_score(left_column, right_column))