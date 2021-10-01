# Loops
* Python supports 2 loops.
  * while 
  * for
  
# while loop
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

## break
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
* Output
```
0
1
2
3
```

## continue
* With this statement, we can stop the current iteration and continue with the next. Try to run this code block,
```
i = 0

while i < 3:
    print("--------------------------------------")
    print("Value before continue: " + str(i))

    i += 1

    if i==2:
        continue
    
    #AFTER CONTINUE WON'T WORK IN THE ITERATION WHICH i=2

    print("Value after continue: " + str(i))
    print("i is not 2 in this iteration.")
```
* Output
```
--------------------------------------
Value before continue: 0
Value after continue: 1
i is not 2 in this iteration.
--------------------------------------
Value before continue: 1
--------------------------------------
Value before continue: 2
Value after continue: 3
i is not 2 in this iteration.
```
## else
* This statement will run when while condition is no longer True.

```
i = 0

while i < 5:
  print(i)
  i += 1
else:
  print("---------------------------")
  print("i is no longer less than 5.")
```
* Output
```
0
1
2
3
4
---------------------------
i is no longer less than 5.
```
* For further reading, you can check the [original Python document about while loops.](https://wiki.python.org/moin/WhileLoop)

# for loop
* We can use a for loop for iterating over an iteratable object such as lists, dictionaries, tuples, sets or even strings.
* range() function gets 2 inputs. Returns values starting from first input to second input. If we give only 1 input to this function, it gets starting value as 0 by default.

```
for x in range(0, 5):
    print("This is iteration number " + str(x))
```

this equals to

```
x = 0
while x < 5:
    print("This is iteration number " + str(x))
    x += 1
```

## looping over a List
```
animals = ["turtle", "fish", "bird", "fox"]
for x in animals:
    print("This is iterations animal is " + x + ".")
```

## looping over a String
```
string = "Hello world!"
for x in string:
    print(x)
```

### Note: You can use the break, continue and else statements same as while loops.

* For further reading, you can check the [original Python document about for loops.](https://wiki.python.org/moin/ForLoop)

#
* See you on the next document!