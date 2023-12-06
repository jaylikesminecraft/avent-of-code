import re

x = []
with open("./day 1/list.txt", 'r') as list:
    x = list.read()

strings = x.split()

sum = 0

for string in strings:
    numbers = re.findall(r"\d+", string)
    numbers = "".join(numbers)
    sum += int(numbers[0] + numbers[len(numbers)-1])

print(sum)