

floaters = [4, 6, 9, 12, 33, 66, 99]

for f in floaters:
    print(f)

print()
print()
floaters.sort()
floaters.reverse()
for x in floaters:
    if x % 2 != 0:
        print(x)

