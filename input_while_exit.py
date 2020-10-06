"""
Program:exiting loops
Author: Avery Tilley
Last date modified: 9/28/20




"""



listVar = []
sentVar = -1
exitVar = -2
n = 0
while n != sentVar:
    n = int(input('Enter value between 1 and 100(-1 to stop inputing values and -2 to quit the program)'))

    if (n<1 or n >100) and (n != -1):
        print('input not in valid range try again')
    elif n != sentVar:
        listVar.append(n)

for i in listVar:
    print(i)

"""
I am unsure on this one. I think I read the question as having two while loops and using break with another sentinal value to break out of it to close the program.
I only have one while loop so I am unsure on how to progress. 
"""
