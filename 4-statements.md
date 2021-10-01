# Statements
## if statement
* If we want our code block to run under a specified condition, we use an "if" statement.
```
friends = ["Cem", "Sinem", "Ceren", "Ege"]
family = ["Arda", "Ares", "Dogan", "Ferda"]


if "Cem" in family:     #False
    print("This is not going to be printed.")

if "Cem" in friends:    #True
    print("This is going to be printed.")
```

## elif statement
* This statement is used for if other conditions fail, then check this condition.
```
friends = ["Cem", "Sinem", "Ceren", "Ege"]
family = ["Arda", "Ares", "Dogan", "Ferda"]


if "Ceren" in family:       #False
    print("This is not going to be printed.")

elif "Ceren" in friends:    #True
    print("This is going to be printed.")

elif "Ares" in friends:     #True
    print("This is not going to be printed. Even if the condition is True.") 
```
* Because, the condition above is True and it will print out. That means other conditions didn't fail.

## else statement
* This statement is for if all other conditions fail, then do this. "else" has no condition for itself. It covers all possibilities except other conditions. 
```
friends = ["Cem", "Sinem", "Ceren", "Ege"]
family = ["Arda", "Ares", "Dogan", "Ferda"]


if "Ceren" in family:       #False
    print("This is not going to be printed.")

elif "Arda" in friends:     #False
    print("This is not going to be printed.")

elif "Sinem" in Family:     #False
    print("This is not going to be printed.") 

else:
    print("This is going to be printed.")
```

## Short "if" and "else" statements
* There is a short way to implement "if" statements if we have only one statement.
```
x=10
y=5

if x > y: print("x is greater than y.")
```
or
```
x = 32
y = 124

print("x is greater than y.") if x > y else print("y is greater than x.")
```

### Note:
* You cannot leave an if statement empty. If you want to pass a specific condition, you can use "pass" statement.
* You can put an if statement inside another if statement.

```
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if 1 in x:
    if 2 in x:
        pass

    else:
        print("1 is in list and 2 is not in the list.") # this won't print out
```
* If you remove 2 from the list, then it will print out.

#
* See you on the next document!