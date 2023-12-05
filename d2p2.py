def main():
    total = 0
    with open("input2.txt", "r") as input:
        for line in input:
            total += check(line)
    print(total)

def check(line):
    r = 0
    g = 0
    b = 0
    remove_index = line.index(":")
    s = line[remove_index + 2:]
    array = s.split(" ")
    for i in range(int(len(array) / 2)):
        number = int(array[i*2])
        color = array[i*2 + 1]
        if "red" in color and number > r:
            r = number
        if "green" in color and number > g:
            g = number
        if "blue" in color and number > b:
            b = number
    return(r * g * b)

if __name__ == "__main__":
    main()
