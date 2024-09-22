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




## Data Types

### Built-in Data Types
Python has the following data types built-in by default, in these categories: 
- Text Type: 	  >>>    str
- Numeric Types:  >>>    int, float, complex
- Sequence Types: >>>    list, tuple, range
- Mapping Type:   >>>    dict
- Set Types: 	  >>>    set, frozenset
- Boolean Type:   >>>    bool
- Binary Types:   >>>    bytes, bytearray, memoryview
- None Type: 	  >>>    NoneType

To get the data type : use the <b>type()</b>  function.

NOTE: The data type gets assigned by python itself. If you want to assign it by yourself. You have to type it like: 
```python
x = str("Hello Fuckers")
```
### Numbers
There are three numeric types in Python: 
- int
- float
- complex
```python
x = 1    # int
y = 2.8  # float
z = 1j   # complex # j is not accidentally there. That's why it's complex number
``` 
You can convert int to float and float to int or int and float to complex but you can't complex to any other. ! ! !  
#### Int

Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
#### Float
Float

Float, or "floating point number" is a number, positive or negative, containing one or more decimals. 
#### Complex
Complex numbers are written with a "j" as the imaginary part.

#### Randome Number
Python does not have a random()function but it has a module called random. just import it and than you can use it to get a random number.
```python
import random
print(random.randrange(1, 10))
```
### Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello". 
You can use quotes inside a string, as long as they don't match the quotes surrounding the string 
#### Multiline Strings
You can assign a multiline string to a variable by using three quotes or three single quotes: 
```python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
```
#### Strings are Arrays
Square brackets can be used to access elements of the string.
```python
a = "Hello, World!"
print(a[1])
```
Since strings are arrays, we can loop through the characters in a string, with a for loop.
```python
for x in "banana":
    print(x)
```
#### String Length

To get the length of a string, use the len() function.
```python
len(x)
```
#### Check String
To check if a certain phrase or character is present in a string, we can use the keyword in. 
```python
txt = "The best things in life are free!"
print("free" in txt)  # This will return True or False.
```

You can use it the opposite way as well. just with : 
```python
txt = "The best things in life are free!"
print("expensive" not in txt)
```
