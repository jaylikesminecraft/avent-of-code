import re

x = []
with open("./day 2/list.txt", 'r') as list:
    x = list.read()

strings = x.split()

#regexs = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

regexs = r"one|two|three|four|five|six|seven|eight|nine|\d+"

sum = 0

def wordToInt(word):
    word = str(word)
    match word:
        case "one":
            return "1"
        case "two":
            return "2"
        case "three":
            return "3"
        case "four":
            return "4"
        case "five":
            return "5"
        case "six":
            return "6"
        case 'seven':
            return "7"
        case "eight":
            return "8"
        case "nine":
            return "9"
        case _:
            return word


for string in strings:

    numbersList = ""
    allNumbers = re.findall(regexs, string)
    for word in allNumbers:
        numbersList += wordToInt(word)
    sum += int(numbersList[0] + numbersList[len(numbersList)-1])

print(sum)





