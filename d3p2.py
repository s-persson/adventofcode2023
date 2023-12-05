gears = {
    
}

with open ("input3.txt", "r") as input:
    map = input.readlines()
    height = len(map)
    length = len(map[0]) - 1
    #first value is y, second is x
def main():
    total = 0
    s = ""
    for row in range(len(map)):
        next_correct = False
        next_position = (0, 0)
        for column in range(len(map[row])):
            c = map[row][column]
            if c.isdigit():
                s += c
                if next_correct == False and position_gear(row, column):
                    next_position = position_gear(row, column)
                    next_correct = True
            if not c.isdigit() and s != "":
                if next_correct:
                    if next_position in gears:
                        sum = gears[next_position] * int(s)
                        total += sum
                    else:
                        gears[next_position] = int(s)
                    next_correct = False
                s = ""
    print(total)

def position_gear(r, c):
    for x in range(3):
        for y in range(3):
            a = get_char(r - 1 + x, c - 1 + y)
            if a == "*":
                return (r - 1 + x, c - 1 + y)
    return False
def get_char(r, c):
    if r < 0 or c < 0 or r > height or c > length - 1:
        return (".")
    try:
        return(map[r][c])
    except:
        return (".")
if __name__ == "__main__":
    main()
