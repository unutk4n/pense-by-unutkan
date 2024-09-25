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

#### Slicing Strings

You can return a range of characters by using the slice syntax.
```python
b = "Hello, World!"
print(b[2:5])
```
Slice From the Start 
```python
b = "Hello, World!"
print(b[:5]) # Do the reversed version to slice it to the end
```

#### Modify Strings


```python
a = "Hello, World!"
print(a.upper())
```

```python
a = "Hello, World!"
print(a.lower())
```

```python
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!" 
```

```python
a = "Hello, World!"
print(a.replace("H", "J"))
```
```python
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'] 
```

#### F-Strings

F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations. 

```python
 age = 36
txt = f"My name is John, I am {age}"
```
#### Placeholders and Modifiers

A placeholder can contain variables, operations, functions, and modifiers to format the value. 

A placeholder can include a modifier to format the value.

A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals: 
```python
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
```
A placeholder can contain Python code, like math operations: 
```python
 txt = f"The price is {20 * 59} dollars"
print(txt)
```
#### Escape Characters

To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.

```python
txt = "We are the so-called \"Vikings\" from the north."
```

Other Escape Characters

- \'   	Single Quote 	
- \\ 	  Backslash 	
- \n 	  New Line 	
- \r   	Carriage Return 	
- \t 	  Tab 	
- \b  	Backspace 	
- \f  	Form Feed 	
- \ooo 	Octal value 	
- \xhh 	Hex value


#### String Methods
<b>Note: All string methods return new values. They do not change the original string.</b>

https://www.w3schools.com/python/python_strings_methods.asp 


### Booleans
ou can evaluate any expression in Python, and get one of two answers, True or False. 

When you compare two values, the expression is evaluated and Python returns the Boolean answer: 
```python
print(10 > 9)
print(10 == 9)
print(10 < 9) 
```

When you run a condition in an if statement, Python returns True or False: 
```python
 a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") 
```

Most Values are True

Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones. 


These are false:
```python
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) 
```

## Python Operators

Python divides the operators in the following groups:

-  Arithmetic operators
-  Assignment operators
-  Comparison operators
-  Logical operators
-  Identity operators
-  Membership operators
-  Bitwise operators
  

### Python Arithmetic Operators

- \+ 	Addition       	x + y 	
- \- 	Subtraction 	  x - y 	
- \* 	Multiplication 	x * y 	
- / 	Division 	      x / y 	
- % 	Modulus 	      x % y 	
- ** 	Exponentiation 	x ** y 	
- \// Floor division 	x // y

### Python Assignment Operators


- = 	   x = 5 	        x = 5 	
- += 	   x += 3 	      x = x + 3 	
- -= 	   x -= 3       	x = x - 3 	
- *=     x *= 3       	x = x * 3 	
- /= 	   x /= 3 	      x = x / 3 	
- %= 	   x %= 3 	      x = x % 3 	
- //= 	 x //= 3 	      x = x // 3 	
- **= 	 x **= 3 	      x = x ** 3 	
- &= 	   x &= 3 	      x = x & 3 	
- |= 	   x |= 3 	      x = x | 3 	
- ^= 	   x ^= 3 	      x = x ^ 3 	
- \>>= 	 x >>= 3 	      x = x >> 3 	
- <<= 	 x <<= 3 	      x = x << 3 	
- := 	   print(x := 3) 	x = 3
  

### Python Comparison Operators

- == 	  Equal 	                  x == y 	
- != 	  Not equal 	              x != y 	
- \> 	  Greater than 	            x > y 	
- \<   	Less than               	x < y 	
- \>= 	Greater than or equal to 	x >= y 	
- <=  	Less than or equal to 	  x <= y

### Logical Operators

- and
- or
- not

### Identity Operators

- is
- is not


### Membership Operators
- in
- not in


### Bitwise Operators

- &  	AND 	Sets each bit to 1 if both bits are 1 	x & y 	
- | 	OR 	Sets each bit to 1 if one of two bits is 1 	x | y 	
- ^ 	XOR 	Sets each bit to 1 if only one of two bits is 1 	x ^ y 	
- ~ 	NOT 	Inverts all the bits 	~x 	
- << 	Zero fill left shift 	Shift left by pushing zeros in from the right and let the - leftmost bits fall off 	x << 2 	
- \>> 	Signed right shift 	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off 	x >> 2


### Operator Precedence
You should also take a note of the precedence thing.


## Lists

Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets: 
```python
 thislist = ["apple", "banana", "cherry"]
 ```

 List items are ordered, changeable, and allow duplicate values. 

List items are indexed, the first item has index [0], the second item has index [1] etc. 

### Ordered
When we say that lists are ordered, it means that the items have a defined order, and that order will not change. 

If you add new items to a list, the new items will be placed at the end of the list. 
### Changeable
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created. 
### Allow Duplicates
Since lists are indexed, lists can have items with the same value 
### List Length
To determine how many items a list has, use the len() function:
### List Items - Data Types
List items can be of any data type: 
```python
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
```
A list can contain different data types: 
```python
list1 = ["abc", 34, True, 40, "male"]
```
### type()

From Python's perspective, lists are defined as objects with the data type 'list':
```python
<class 'list'> 
```
### The list() Constructor

It is also possible to use the list() constructor when creating a new list. 

Using the list() constructor to make a List:
```python
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
```

### Using the list() constructor to make a List:
```python
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
```

### Access List Items
List items are indexed and you can access them by referring to the index number: 
```python
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
```
### Check if Item Exists 
```python
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") 
```
### Change Item Value
 
To change the value of a specific item, refer to the index number: 
```python
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
```
### Change a Range of Item Values
```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
```
### Insert Items
The insert() method inserts an item at the specified index: 
```python
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
```

### Add List Items

#### Append Items

To add an item to the end of the list, use the append() method: 


#### Insert Items

To insert a list item at a specified index, use the insert() method.

The insert() method inserts an item at the specified index:
```python
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
```
#### Extend List

To append elements from another list to the current list, use the extend() method. 

```python
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
```
<b> The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).</b> 

### Remove List Items

#### Remove Specified Item

The remove() method removes the specified item. 
```python
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
```
<b> If there are more than one item with the specified value, the remove() method removes the first occurrence:</b> 

#### Remove Specified Index 
The pop() method removes the specified index. 

```python
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
```
<b> If you do not specify the index, the pop() method removes the last item. </b>
The del keyword also removes the specified index:  

```python
thislist = ["apple", "banana", "cherry"]
del thislist[0]
```
<b> The del keyword can also delete the list completely.</b> 

```python 
thislist = ["apple", "banana", "cherry"]
del thislist 
```
#### Clear the List
 The clear() method empties the list.

The list still remains, but it has no content. 

```python
thislist = ["apple", "banana", "cherry"]
thislist.clear()
``` 


### Loop Lists

#### Loop Through a List
You can loop through the list items by using a for loop: 
```python
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) 
  ```

#### Loop Through the Index Numbers

You can also loop through the list items by referring to their index number.

Use the <b>range()</b>  and <b>len()</b> functions to create a suitable iterable. 

```python
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i]) 
```
#### Using a While Loop 

ou can loop through the list items by using a while loop. 

```python
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
```

### List Comprehension

List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside: 

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) 
```
With list comprehension you can do all that with only one line of code: 

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist) 
```
### Sort Lists
#### Sort List Alphanumerically 

```python
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
```
#### Sort Descending

```python
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
```
#### Customize Sort Function

You can also customize your own function by using the keyword argument key = function. 
```python
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
```

<b> NOTE : By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters: </b>
Luckily we can use built-in functions as key functions when sorting a list.

So if you want a case-insensitive sort function, use str.lower as a key function 

```python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
```
### Copy Lists

You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2. 
 
You can use the built-in List method copy() to copy a list. 
```python
 thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
```
#### Use the list() method
```python
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
```
#### Use the slice Operator
```python
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
```

### Join Lists
There are several ways to join, or concatenate, two or more lists in Python.

One of the easiest ways are by using the + operator. 

```python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
```

you can use the extend() method, where the purpose is to add elements from one list to another list: 
```python
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
```

### List Methods
Python has a set of built-in methods that you can use on lists. 

- append()	Adds an element at the end of the list
- clear()	Removes all the elements from the list
- copy()	Returns a copy of the list
- count()	Returns the number of elements with the specified value
- extend()	Add the elements of a list (or any iterable), to the end of the current list
- index()	Returns the index of the first element with the specified value
- insert()	Adds an element at the specified position
- pop()	Removes the element at the specified position
- remove()	Removes the item with the specified value
- reverse()	Reverses the order of the list
- sort()	Sorts the list


## Tuples

```python
mytuple = ("apple", "banana", "cherry")
```
- Tuples are used to store multiple items in a single variable.

- Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

- A tuple is a collection which is ordered and unchangeable.

- Tuples are written with round brackets.
### Tuple Items

Tuple items are ordered, unchangeable, and allow duplicate values. 

### Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change. 
### Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created. 
### Allow Duplicates
Since tuples are indexed, they can have items with the same value: 
### Create Tuple With One Item
To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple. 
```python
thistuple = ("apple",)
```
### Data Types

Tuple items can be of any data type 
A tuple can contain different data types 
### type()
From Python's perspective, tuples are defined as objects with the data type 'tuple': 
```python
<class 'tuple'> 
```
### The tuple() Constructor
 It is also possible to use the tuple() constructor to make a tuple. 
```python
 thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
 ```
<b>IMPORTANT</b>
 
### Python Collections (Arrays)

There are four collection data types in the Python programming language:

    List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    Dictionary is a collection which is ordered** and changeable. No duplicate members.

ACCESS TUPLES BASLIGINDA KALDIK



