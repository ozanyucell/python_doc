# Lists
* Lists are used to store multiple data in a single variable. This is similar to arrays that exist in many other programming languages.
* We are creating lists with square brackets:

```
list_name = ["variable_0", "variable_1", "variable_2", "variable_3"]
```
* Note that lists may store different data types.
```
x = [19, "Ela", False, "female"] # This array stores integer, String and boolean variables.
```
* It is also possible to create lists with list() constructor.
```
list_name = list(("variable_0", "variable_1", "variable_2", "variable_3"))
```

# Indexes
* List's data are indexed by starting from 0. So,
```
variable_0 => 0. index
variable_1 => 1. index
variable_2 => 2. index
variable_3 => 3. index
```

* Python also supports negative indexing,
```
variable_0 =>  0. index
variable_1 => -3. index
variable_2 => -2. index
variable_3 => -1. index
```

# Length of a list
* To determine length of our list we should use len() function.
```
tv_series = ["mr_robot", "breking_bad", "rick_and_morty", "vikings"]
print(len(tv_series))
```
* We should see the output as "4".

# Accesing the data
* We can access to data with square brackets and index number.
```
games = ["Rainbow 6 Siege", "Metro Exodus", "The Witcher 3", "Red Dead Redemption 2", "Soma"]
print(games[1])
```
* This should print Metro Exodus. We can use negative indexing as well.
```
games = ["Rainbow 6 Siege", "Metro Exodus", "The Witcher 3", "Red Dead Redemption 2", "Soma"]
print(games[-1])
```
* This should print Soma now.
* We can print out multiple data with **:** operator.
```
games = ["Rainbow 6 Siege", "Metro Exodus", "The Witcher 3", "Red Dead Redemption 2", "Soma"]
print(games[1:4])
```
* This will print index 1, index 2 and index 3 but not index 4. So, we should see Metro Exodus, The Witcher 3 and Red Dead Redemption 2 on our terminal.
* By leaving empty one side of the operator, the range will go on to the end of the list.
```
games = ["Rainbow 6 Siege", "Metro Exodus", "The Witcher 3", "Red Dead Redemption 2", "Soma"]
print(games[:3])
```
* This will print out index 0, index 1 and index 2.

# Checking if a variable exists in the list
* For checking a variable is in a list or not,
```
movies = ["Sicario", "Interstellar", "Arrival"]
if "Arrival" in thislist:
  print("Arrival is in the list.")
else:
  print("Arrival is not in the list.")
```