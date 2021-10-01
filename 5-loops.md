# Loops
* Python supports 2 loops.
  * while 
  * for
  
## while loop
* We need to give a condition to our while loop. As long as that condition is true, while loop will continue.

```
i = 0

while i < 5:
  print(i)
  i += 1    # this will increase the value of i by 1.
```
* This will print i until i becomes greater than 5.
* If you have implemented loop like,
```
i = 0

while i < 5:
  print(i)
```
there wouldn't be anything to make while's condition True. Then you would have created an infinite loop which prints an infinite number of 0s.
* We can modify our while loops with statements. Let's talk about them in more detail.

### break
* With this statement, we can stop the loop even the while condition is True.
```
i = 0

while i < 5:
  print(i)
  i += 1
  if i == 4:
    break
```
* Now this will only print 0, 1, 2 and 3. Because we told it to break the loop if i equals to 4.

### continue
* With this statement, we can stop the current iteration and continue with the next. Try to run this code block,
```
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
```

### else
* 

## for loop

