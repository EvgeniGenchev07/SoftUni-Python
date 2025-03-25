cards = list(input().split(', '))
n = int(input())
for _ in range(n):
    cmd = list(input().split(', '))
    if cmd[0] == "Add":
        if cards.__contains__(cmd[1]):
            print("Card is already in the deck")
        else:
            cards+=[cmd[1]]
            print("Card successfully added")
    elif cmd[0] == "Remove":
        try:
            cards.remove(cmd[1])
            print("Card successfully removed")
        except ValueError:
            print("Card not found")
    elif cmd[0] == "Insert":
        index = int(cmd[1])
        if index >= len(cards):
            print("Index out of range")
        elif cards.__contains__(cmd[2]):
            print("Card is already added")
        else:
            cards.insert(index,cmd[2])
            print("Card successfully added")
    elif cmd[0] == "Remove At":
        index = int(cmd[1])
        if index >= len(cards):
            print("Index out of range")
        else:
            cards.pop(index)
            print("Card successfully removed")
print(', '.join(cards))
