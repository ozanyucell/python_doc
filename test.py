i = 0

while i < 3:
    print("--------------------------------------")
    print("Value before continue:" + str(i))
    i += 1
    if i==2:
        continue
    #AFTER CONTINUE WON'T WORK IN THE ITERATION WHICH i=2
    print("Value after continue: " + str(i))
    print("i is not 2 in this iteration.")