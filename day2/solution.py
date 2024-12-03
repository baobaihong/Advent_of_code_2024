## Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.
with open('day1/input.txt', 'r') as file:
    # Split and convert to int in one go
    left_column, right_column = zip(*(
        map(int, line.split()) for line in file
    ))

def calculate_similarity_score(left_column, right_column):
    similarity_score = 0
    for i in range(0, len(left_column)):
        similarity_score += left_column[i] * right_column.count(left_column[i])
    return similarity_score

print(calculate_similarity_score(left_column, right_column))