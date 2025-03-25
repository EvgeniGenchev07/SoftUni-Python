n = int(input())
total = 0
for i in range(1,n+1):
    city = input()
    profit = float(input())
    expences = float(input())
    if i % 5 == 0:
        profit -= profit * 0.1 + expences
    elif i % 3==0:
        profit -= expences + expences * 0.5
    else:
        profit -= expences
    print(f"In {city} Burger Bus earned {profit:.2f} leva.")
    total += profit
print(f"Burger Bus total profit: {total:.2f} leva.")
