colours = {
    "red" : 12,
    "green" : 13,
    "blue" : 14
}
def main():
    total = 0
    with open("input2.txt", "r") as input:
        for line in input:
            total += check(line)
    print(total)

def check(line):
    id = int(line[5:8].replace(":", ""))
    remove_index = line.index(":")
    s = line[remove_index + 2:]
    array = s.split(" ")
    for i in range(int(len(array) / 2)):
        number = int(array[i*2])
        color = array[i*2 + 1]
        for x in colours:
            if x in color:
                max = colours[x]
                if number > max:
                    return (0)
    return(id)

if __name__ == "__main__":
    main()
