import re

def find_numbers_in_order(s):
    numbers = re.findall(r'\d+', s)
    ordered_numbers = sorted(numbers, key=lambda x: s.index(x))
    return ordered_numbers