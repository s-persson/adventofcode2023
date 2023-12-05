with open("input1.txt", "r") as input:
    total = 0
    for line in input:
        first = ""
        last = ""
        for char in line:
            if char.isdigit():
                if first == "":
                    first = char
                last = char
        total += (int(first + last))
print(total)
        
                
