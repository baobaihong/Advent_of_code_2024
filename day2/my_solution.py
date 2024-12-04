## The unusual data (your puzzle input) consists of many reports, one report per line. 
## Each report is a list of numbers called levels that are separated by spaces.

## a report only counts as safe if both of the following are true:
## 1. The levels are either all increasing or all decreasing.
## 2. Any two adjacent levels differ by at least one and at most three.

## How many reports are safe?

with open('day2/input.txt', 'r') as file:
    report_list = [list(map(int, line.split())) for line in file]


def is_report_safe(list):
    length = len(list)
    first_differ = list[1] - list[0]
    if first_differ > 0 and first_differ <= 3:
        is_increasing = True
    elif first_differ < 0 and first_differ >= -3:
        is_increasing = False
    else:
        return False, 1
        
    for i in range(2, length):
        differ = list[i] - list[i - 1]
        if differ > 3 or differ < -3:
            return False, i
        else:
            if is_increasing and differ <= 0:
                return False, i
            elif not is_increasing and differ >= 0:
                return False, i
            else:
                continue
    
    return True, None

safe_num = 0
# for report in report_list:
#     if is_report_safe(report):
#         safe_num += 1
        
# print(safe_num)

# part2: safe report with damper
def is_report_safe_dampener(report: list):
    is_safe_first, wrong_level = is_report_safe(report)
    if is_safe_first:
        return True
    else:
        report_copy_1 = report.copy()
        report_copy_1.pop(wrong_level)
        is_safe_second_1, _ = is_report_safe(report_copy_1)
        if is_safe_second_1:
            print(f"original {report} is unsafe")
            print(f"1st round {report_copy_1} is safe \n")
            return True
        else:
            report_copy_2 = report.copy()
            report_copy_2.pop(wrong_level - 1)
            is_safe_second_2, _ = is_report_safe(report_copy_2)
            if is_safe_second_2:
                print(f"original {report} is unsafe")
                print(f"2nd round {report_copy_2} is safe \n")
                return True
            else:
                return False
            
            
def is_report_safe_dampener_v2(report: list):
    is_safe_first, wrong_level = is_report_safe(report)
    if is_safe_first:
        return True
    else:
        for i in range(0,len(report)):
            report_copy = report.copy()
            report_copy.pop(i)
            is_safe_second_2, _ = is_report_safe(report_copy)
            if is_safe_second_2:
                print(f"original report: {report} unsafe\nsecond round {report_copy} is safe")
                return True
            else:
                continue
        return False
            
for report in report_list:
    if is_report_safe_dampener_v2(report):
        safe_num += 1
        
print(safe_num)