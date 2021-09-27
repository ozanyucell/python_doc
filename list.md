# Lists
* Lists are used to store multiple data in a single variable. This is similar to arrays that exist in many other programming languages.
* We are creating lists with square brackets:

```
list_name = ["variable_0", "variable_1", "variable_2", "variable_3"]
```
* Note that lists may store different data types.
```
x = [19, "Ela", False, "female"] #This array stores integer, String and boolean variables.
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

# len()
* We can determine how many items we have in our list by using len() function.
```
tv_series = ["mr_robot", "breking_bad", "rick_and_morty", "vikings"]
print(len(tv_series))
```
* We should see the output as "4".

