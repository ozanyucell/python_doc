########## NO INFORMATION FOR "is" OPERATOR

# Conditions
* We can use the usual logical conditions from math.
  * x == y (Equals)
  * x > y  (Greater than)
  * x < y  (Less than)
  * x >= y (Greater than or equal to)
  * x <= y (Less than or equal to)
  * x != y (Not equals)

* These conditions returns boolean values which can only be True or False.
* We will use these conditions on many places. Mostly on **loops** and **if-elif-else statements**.

## and operator
* "and" operator returns True only if both sides of the operator satisfies the condition.
```
name = "Ela"
age = 19
print(name == "Ela" and age == 19)
```
This will print True.
```
name = "Ela"
age = 19
print(name == "Ela" and age == 22)
```
This will print False.

## or operator
* "or" operator returns True only if one side of the operator satisfies the condition.
```
name = "Ela"
age = 19
print(name == "Ela" or age == 20)
```
This will print True.
```
name = "Ela"
age = 19
print(name == "Ozan" or age == 22)
```
This will print False.

## in operator
* in operator checks if the specified object is in an iterable object or not.

```
movies = ["Sicario", "Interstellar", "Arrival"]
print("Inception" in movies)
```
This should return False because "Inception" is not in the list.

## is operator
* 

## not operator
* This basically inverts the any boolean value.
```
print(not False) #prints out True
```
More complex example:
```
name = "Ela"
age = 19
print(not(name == "Ozan" and age == 22))
```
Now this should print out True.

#
* See you on the next document!