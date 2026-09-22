n = int(input("in_1: "))

och = 0
zaoch = 0

for i in range(n):
    sn, name, age, form = input(f"in_{i+2}: ").split()
    if form == "True":
        och += 1
    else:
        zaoch += 1

print("out:", och, zaoch)