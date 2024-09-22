# PYTHON DOCUMENTS

## Syntax
Indentation refers to the spaces at the beginning of a code line. 
The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one. 

## Comments
Comments starts with a #, and Python will ignore them 
Or, not quite as intended, you can use a multiline string. """ COMMENT """

## Variables
Variables are containers for storing data values.

### Creating Variables

Python has no command for declaring a variable.
You can use either single or double quotes.
Variable names are case sensitive. 
A variable is created the moment you first assign a value to it. 
```python
x = 5
y = "John"
```
### Casting 
If you want to specify the data type of a variable, this can be done with casting. 
```python
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 
```
### Naming
- Camel Case >>> firstSmallThanBig
- Pascal Case >>> EveryOneBig
- Snake Case line_between_them

### Assign Multiple Values
```python
x, y, z = "Orange", "Banana", "Cherry"
```
you can assign the same value to multiple variables in one line: 
```python
x = y = z = "Orange"
```

### Unpacking a Collection
```python 
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits # This will assign each element to each variable
```

### Output Variables

The Python print() function is often used to output variables.
```python
print(x)
```
You can print more than one variable, just don't forgot to seperate them by a comma. 


### Global Variables
Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables. 

Global variables can be used by everyone, both inside of functions and outside. 
<b>the global keyword<b>

Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.
```python
def myfunc():
  global x
  x = "fantastic"
```
Also, use the global keyword if you want to change a global variable inside a function. 
```python
x = "awesome"

def myfunc():
  global x
  x = "fantastic"
```


