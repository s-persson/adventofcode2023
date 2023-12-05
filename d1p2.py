with open("input1.txt", "r") as input:
    numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    total = 0
    for line in input:
        first = ""
        last = ""
        for charI in range(len(line)):
            if line[charI].isdigit():
                if first == "":
                    first = line[charI]
                last = line[charI]
            else:
                number = ""
                if ''.join(line[charI:charI+3]) in numbers:
                    number = numbers[''.join(line[charI:charI+3])]
                if ''.join(line[charI:charI+4]) in numbers:
                    number = numbers[''.join(line[charI:charI+4])]
                if ''.join(line[charI:charI+5]) in numbers:
                    number = numbers[''.join(line[charI:charI+5])]
                if number != "":           
                    if first == "":
                        first = number
                    last = number

        x = str(first) + str(last)
        total += int(x)   
print(total)
