#ID & Amount of winning numbers
starting_cards = {}
all_cards = []

def main():
    total = 0
    with open("input4.txt", "r") as input:
        for line in input:
            add_card(line)
    for card in all_cards:
        get_clones(card[0], card[1])
    print(len(all_cards))

def add_card(line):
    a = line[5:8]
    id = a.replace(":", " ").strip()
    s = line[8:]
    winning, check = s.split("|")
    winlist = []
    checklist = []
    for a in winning.split(" "):
        if a != "":
            winlist.append(a.strip())
    for a in check.split(" "):
        if a != "":
            checklist.append(a.strip())
    amount_wins = get_amount_win(winlist, checklist)
    starting_cards[id] = amount_wins
    all_cards.append((id, amount_wins))

def get_amount_win(winlist, checklist):
    amount_wins = 0
    for check in checklist:
        if check in winlist:
            amount_wins += 1
    return amount_wins

def get_clones(id, amount_wins):
    for i in range(amount_wins):
        if int(id) + i < len(starting_cards):
            key = str(int(id) + i + 1)
            all_cards.append((key, starting_cards[key]))
    

if __name__ == "__main__":
    main()
