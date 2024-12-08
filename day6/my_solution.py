## PART1
# Map: ^ for guard(direction of arrow = facing) and # for obstacles
# Rules for the guard:
# 1.If there is something directly in front of you, turn right 90 degrees.
# 2.Otherwise, take a step forward.
# Predict the path of the guard. 
# Question: How many distinct positions will the guard visit before leaving the mapped area? (Including the guard's starting position)

def navigator(map: list[list[str]]):
    guard = '^'    # Store the status of the guard
     
    # Calculate the width and height of map
    map_height = len(map) - 1
    map_width = len(map[0]) - 1
    
    # Find the position of guard
    for y, line in enumerate(map):
        for x, element in enumerate(line):
            if element == guard:
                current_x = x
                current_y = y
   
    # Calculate guard's next move based on its facing direction
    # hit_obstacle = 0
    steps = 0
    while True:
        # print(f"Step {steps}: Guard at ({current_x}, {current_y}) facing {guard}")
        # Calculate the potential next step
        if guard == '^' and current_y != 0:
            next_x = current_x
            next_y = current_y - 1
        elif guard == '>' and current_x != map_width:
            next_x = current_x + 1
            next_y = current_y
        elif guard == 'v' and current_y != map_height:
            next_x = current_x
            next_y = current_y + 1
        elif guard == '<' and current_x != 0:
            next_x = current_x - 1 
            next_y = current_y
        
        # move one step forward
        if map[next_y][next_x] != '#' and map[next_y][next_x] != 'O':
            steps += 1
            map[current_y][current_x] = 'X'
            map[next_y][next_x] = guard
            current_x = next_x
            current_y = next_y
        
        # turn the guard to its right
        elif map[next_y][next_x] == '#' or map[next_y][next_x] == 'O': 
            # if map[next_y][next_x] == 'O':
                # hit_obstacle += 1
            if guard == '^':
                guard = '>'
            elif guard == '>':
                guard = 'v'
            elif guard == 'v':
                guard = '<'
            elif guard == '<':
                guard = '^'
        
        # Stop the function and return the map
        if (guard == '^' and current_y == 0) or (guard == '>' and current_x == map_width) or (guard == 'v' and current_y == map_height) or (guard == '<' and current_x == 0):
            map[current_x][current_y] = 'X'
            return map, "walk out"
        # if hit_obstacle > 3:
        #     return map, "loop"
        # Add maximum step limit
        if steps > 30000:  # Arbitrary limit
            return map, "infinite_loop"
                

def map_decoder(input: str) -> list[list[str]]:
    return [list(line) for line in input.split('\n')]

obstacle_position_loop = 0
obstacle_position_infinite = 0
with open ('day6/input.txt', 'r') as file:
    full_text = file.read()
    map = map_decoder(full_text)
    # map_with_path = navigator(map)

# path_count = 0
# for line in map_with_path:
#     for step in line:
#         if step == 'X':
#             path_count += 1
            
# print(f"There are {path_count} 'X' in map.")

## PART2
for y, line in enumerate(map):
    for x, element in enumerate(line):
        if element == '.':
            current_map = [row[:] for row in map] # copy original map
            current_map[y][x] = 'O'
            _, result_str = navigator(current_map)
            print(f"set obstacle at ({y}, {x}) result in {result_str}")
            if result_str == 'loop':
                obstacle_position_loop += 1
            elif result_str == 'infinite_loop':
                obstacle_position_infinite += 1
                
print(f"There are {obstacle_position_loop} loop obstacles and {obstacle_position_infinite} infinite obstacles.")