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
        for column in range(len(map[row])):
            c = map[row][column]
            if c.isdigit():
                s += c
                if next_correct == False and find_valid(row, column):
                    next_correct = True
            if not c.isdigit() and s != "":
                if next_correct:
                    total += int(s)
                    next_correct = False
                s = ""
    if next_correct:
        total += int(s)
    print(total)

def find_valid(r, c):
    for x in range(3):
        for y in range(3):
            a = get_char(r - 1 + x, c - 1 + y)
            if not a.isdigit() and a != ".":
                return True
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
