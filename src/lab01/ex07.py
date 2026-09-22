s = input("in: ")

start = -1
for i in range(len(s)):
    if s[i].isupper():
        start = i
        break

end = s.rfind('.')

second = -1
for i in range(len(s)):
    if s[i].isdigit():
        second = i + 1
        break

step = second - start

result = []
i = start
while i <= end:
    result.append(s[i])
    i = i + step

if result[-1] == '.':
    result.pop()

print("out: " + ''.join(result))