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
* The data of the list is indexed by starting from 0.
```
variable_0 => 0. index
variable_1 => 1. index
variable_2 => 2. index
variable_3 => 3. index
```

* Python also supports negative indexing.
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

# Changing values
* To change any, we should give its index number.
```
movies = ["Sicario", "Interstellar", "Arrival"]
movies[1] = "Matrix"
```
* With this we changed "Interstellar" with "Matrix".
* Also we can use : operator for changing multiple data from our list.
```
tv_series = ["mr_robot", "breking_bad", "rick_and_morty", "vikings"]
tvseries[1:3] = "sherlock"
```
* This will remove index 1 and index 2, then it will insert sherlock to index 1. After operation, list is going to look like this: ["mr_robot", "sherlock", "vikings"]

# Inserting Data
### instert()
* For inserting a new item into our list, we can use instert() function. First, we should define in which index the data will be added, and then the data will be added. 
```
movies = ["Sicario", "Interstellar", "Arrival"]
movies.insert(2, "Inception")
```
* This will insert "Inception" on index 2. At the end, list will have 4 items.

### append()
* There is also a append() method. This method doesn't take index input. Adds the data directly to the end of the list.
```
movies = ["Sicario", "Interstellar", "Arrival"]
movies.append("Inception")
```
* This will add "Inception" at the end of the list. After the operation list will look like: ["Sicario", "Interstellar", "Arrival", "Inception"]

### extend()
* For adding a list on another list, we can use extend() method.
```
games = ["Soma", "Alien Isolation", "Battlefield 1", "Metro Exodus", "Red Dead Redemption 2"]
survival_games = ["Subnautica", "Terraria", "Minecraft"]
games.extend(survival_games)
```

# Deleting Data
### remove()
* For removing values from a list, we can use remove() method.
```
movies = ["Sicario", "Interstellar", "Arrival"]
movies.remove("Sicario")
```
* This will remove "Sicario" from the list. List will look like: ["Interstellar", "Arrival"]

### pop()
* pop() method removes the specified index.
```
movies = ["Sicario", "Interstellar", "Arrival"]
movies.pop(0)
```
* This will also remove "Sicario", and look the same.

### del()
* del() also removes a specified index.
```
movies = ["Sicario", "Interstellar", "Arrival"]
del movies[0]
```
* Again same deletion, same list after the operation. del() method can delete the list too.
```
movies = ["Sicario", "Interstellar", "Arrival"]
del movies
```
* List won't exist after **'del movies'**.

### clear()
* clear() method will remove all the content of list. But list will remain.
```
movies = ["Sicario", "Interstellar", "Arrival"]
movies.clear()
```
* After the operation, list is going to be: []

# Checking if a variable exists in the list
* For checking a variable is in a list or not,
```
movies = ["Sicario", "Interstellar", "Arrival"]
if "Arrival" in movies:
  print("Arrival is in the list.")
else:
  print("Arrival is not in the list.")
```

#
* See you on the next document!