listVar = []
sentVar = -1
n = 0
while n != sentVar:
    n = int(input('Enter value between 1 and 100(-1 to stop)'))

    if (n<1 or n >100) and (n != -1):
        print('input not in valid range try again')
    elif n != sentVar:
        listVar.append(n)

for i in listVar:
    print(i)


