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