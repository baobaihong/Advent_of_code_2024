# Search the word 'XMAS"
# Search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words.

# part 1
import re
def count_horizontal(input_text: str):
    xmas_count = re.findall(r'(?=XMAS)', input_text)
    xmas_reverse_count = re.findall(r'(?=SAMX)', input_text)
    
    return len(xmas_count) + len(xmas_reverse_count)


def count_vertical(input_text: str):
    xmas_v_regex=r'(?=X.{140}M.{140}A.{140}S)'
    xmax_v_reverse_regex=r'(?=S.{140}A.{140}M.{140}X)'
    
    xmas_v_count = re.findall(xmas_v_regex, input_text, re.DOTALL)
    xmas_v_reverse_count = re.findall(xmax_v_reverse_regex, input_text, re.DOTALL)
    
    return len(xmas_v_count) + len(xmas_v_reverse_count)

def count_diagonal(input_text: str):
    xmas_diagonal_r_regex = r'(?=X.{141}M.{141}A.{141}S)'
    xmas_diagonal_r_reverse_regex = r'(?=S.{141}A.{141}M.{141}X)'
    xmas_diagonal_l_regex = r'(?=X.{139}M.{139}A.{139}S)'
    xmas_diagonal_l_reverse_regex = r'(?=S.{139}A.{139}M.{139}X)'
    
    xmas_diagonal_r_count = re.findall(xmas_diagonal_r_regex, input_text, re.DOTALL)
    xmas_diagonal_r_reverse_count = re.findall(xmas_diagonal_r_reverse_regex, input_text, re.DOTALL)
    xmas_diagonal_l_count = re.findall(xmas_diagonal_l_regex, input_text, re.DOTALL)
    xmas_diagonal_l_reverse_count = re.findall(xmas_diagonal_l_reverse_regex, input_text, re.DOTALL)
    return len(xmas_diagonal_r_count) + len(xmas_diagonal_r_reverse_count) + len(xmas_diagonal_l_count) + len(xmas_diagonal_l_reverse_count)


with open ('day4/input.txt', 'r') as file:
    input_text = file.read()
    print(f"There are {count_horizontal(input_text)} 'XMAS' & 'SAMX' in text.")
    print(f"There are {count_vertical(input_text)} vertical 'XMAS' & 'SAMX' in text.")
    print(f"There are {count_diagonal(input_text)} diagonal 'XMAS' & 'SAMX' in text.")
    print(f"There are {count_diagonal(input_text)+count_vertical(input_text)+count_horizontal(input_text)} 'XMAS's in text in total! ")

# part2: find x-mas
def count_xmas(input_text: str):
    patterns = [r'(?=M.S.{139}A.{139}M.S)',
               r'(?=M.M.{139}A.{139}S.S)',
               r'(?=S.S.{139}A.{139}M.M)',
               r'(?=S.M.{139}A.{139}S.M)'
               ]
    total = 0
    for pattern in patterns:
        count = re.findall(pattern, input_text, re.DOTALL)
        total += len(count)
    return total

with open('day4/input.txt', 'r') as file:
    input_text = file.read()
    print(f"There are {count_xmas(input_text)} 'X-MAS' in text!")