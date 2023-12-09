def main():
    #IMPORTANT, WIP code not working at the moment
    sets = []
    unsorted_strength = [[], [], [], [], [], [], []]
    sorted_strength = [[], [], [], [], [], [], []]
    card_strength = {'2' : 0, '3' : 1, '4' : 2, '5' : 3, '6' : 4, '7' : 5, '8' : 6, '9' : 7, 'T' : 8, 'J' : 9, 'Q' : 10, 'K' : 11, 'A' : 12}
    types = {"5": 6, "14" : 5, "23" : 4, "113" : 3, "122": 2, "1112": 1, "11111": 0}
    with open ("input7.txt", "r") as input:
        for line in input:
            split = line.split(" ")
            sets.append((split[0], int(split[1].strip())))
    for set in sets:
        occurances = {}
        cards = set[0]
        for card in cards:
            if card in occurances:
                occurances[card] = occurances[card] + 1
            else:
                occurances[card] = 1
        values = list(occurances.values())
        values.sort()
        string = ''.join(str(e) for e in values)
        if string in types:
            unsorted_strength[types[string]].append(set)
    for sort in unsorted_strength:
        for card in sort:
            print(get_index(sort, card))

def get_index(check_array, check_string):
    list = check_array
    list.reverse()
    previous = ""
    check_index = 0
    for card in list:
        current = check_string[check_index]
        target = card[check_index]
        print(current, target)
    return 0
        

if __name__ == "__main__":
    main()
