n = int(input())

och = 0
zaoch = 0

for i in range(n):
    sn, name, age, form = input().split()
    if form == "True":
        och += 1
    else:
        zaoch += 1

print(och, zaoch)