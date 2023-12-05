def main():
    total = 0
    with open("input4.txt", "r") as input:
        for line in input:
            total += check(line)
    print(total)

def check(line):
    temp = 0
    s = line[8:]
    winning, check = s.split("|")
    winlist = []
    checklist = []
    for a in winning.split(" "):
        winlist.append(a.strip())
    for a in check.split(" "):
        checklist.append(a.strip())
    for to_check in checklist:
        try: 
            if int(to_check) and to_check in winlist:
                if temp == 0:
                    temp = 1
                else:
                    temp *= 2
        except:
            continue
    return temp

if __name__ == "__main__":
    main()
