### Why use Python
- High Level of abstraction, which means
  - focus on the logic rather than details of implementation (usually shorter code)
  - extensive libraries for Scientific Computing
- As a script language
  - to pipeline tasks
  - as an interface for system calls and other programs (e.g. C++)

### A few words on efficiency
> If you can't measure it, you can't improve it. - Peter Drucker

> Premature optimization is the root of all evil. - Donald Knuth

- Algorithms and Data Structures (Part II)
- (GPU) Parallel Computing
- FPGA etc.

### Running Python

- interpreter
```
$ python
>>> 3+2
>>> (50 - 5*6) / 4
>>> 8 / 5 # diff in python2 and python3
>>> 17 % 3
>>> 5 ** 2  # 5 squared
>>> width = 20.1
>>> width
>>> height = 5 * 9
>>> width * height
>>> round(_, 2) # REPL only
>>> exit
```

- execute script
```
$ python hello.py
```
- using debugger (pdb)

[Online Doc](https://docs.python.org/2/library/pdb.html)
[Tutorial](https://pythonconquerstheuniverse.wordpress.com/2009/09/10/debugging-in-python/)

```
$ python debug.py
(Pdb) p a
(Pdb) p b
(Pdb) c
(Pdb) p b
(Pdb) l
(Pdb) a = 'a'
(Pdb) p a
(Pdb) !a = 'a'
...
(Pdb) q
```

### Variables and Statement
Numbers
- Integer
- Float

Bonus: binary representation of
- integers
- Fixed-point numbers
- Floating-point numbers
- [Wikipedia](https://en.wikipedia.org/wiki/Computer_number_format#Binary_number_representation)


| Fixed-point numbers (32-bit) | integer bits | fractional bits |
| ------------- |:-------------:|:-----:|
| 0.500	=	 1⁄2	| 	00000000 00000000 | 10000000 00000000 |
| 1.250	=	 1 1⁄4	| 	00000000 00000001 | 01000000 00000000 |
| 7.375	=	 7 3⁄8	| 	00000000 00000111 | 01100000 00000000 |

String
```
>>> 'spam eggs'  # single quotes
'spam eggs'
>>> 'doesn\'t'  # use \' to escape the single quote...
"doesn't"
>>> "doesn't"  # ...or use double quotes instead
"doesn't"
>>> '"Yes," he said.'
'"Yes," he said.'
>>> "\"Yes,\" he said."
'"Yes," he said.'
>>> '"Isn\'t," she said.'
'"Isn\'t," she said.'

>>> '"Isn\'t," she said.'
'"Isn\'t," she said.'
>>> print '"Isn\'t," she said.'
"Isn't," she said.
>>> s = 'First line.\nSecond line.'  # \n means newline
>>> s  # without print, \n is included in the output
'First line.\nSecond line.'
>>> print s  # with print, \n produces a new line
First line.
Second line.

>>> prefix = 'Py'
>>> prefix + 'thon'

>>> 'xiao' + 'baozi'
>>> 'xiao' 'baozi'
>>> prefix 'baozi'

>>> word = 'Python'
>>> word[0]  # character in position 0
'P'
>>> word[5]  # character in position 5
'n'
>>> word[-1]  # last character
>>> word[2:5]  # characters from position 2 (included) to 5 (excluded)
>>> word[:2] + word[2:]
```

Intro to ideas behind ASCII, Unicode and Hexadecimal
```
>>> u"äöü"
u'\xe4\xf6\xfc'
```

Lists
```
>>> squares = [1, 4, 9, 16, 25]
>>> squares
>>> squares[0]
>>> squares[-1]
>>> squares[-3:]
>>> squares + [36, 49, 64, 81, 100]
>>> len(squares)
>>> x = [['a', 'b', 'c'], [1, 2, 3]]
>>> x[0][1]
```

### Multiple Assignment
```
>>> x, y = 2, 3
>>> x
>>> y
```

```
>>> a, b = 0, 1
>>> while b < 10:
...     print b,
...     a, b = b, a+b
...
```

reserved words
```
and, assert, break, class, continue, def, del, elif,
else, except, exec, finally, for, from, global, if,
import, in, is, lambda, not, or, pass, print, raise,
return, try, while
```

### Control flow I： `while`, `if`, `for`, `range`
See example code in `2_control_flow_a`

### Coding Style
[Official Guide](https://docs.python.org/2.7/tutorial/controlflow.html#intermezzo-coding-style)
- Use 4-space indentation, and **no tabs**.
- Wrap lines so that they don’t exceed 79 characters.
- Use blank lines to separate functions and classes, and larger blocks of code inside functions.
- When possible, put comments on a line of their own.
- Use docstrings.
- Use spaces around operators and after commas, but not directly inside bracketing constructs: `a = f(1, 2) + g(3, 4)`.
- Name your classes and functions consistently; the convention is to use CamelCase for classes and lower_case_with_underscores for functions and methods. Always use self as the name for the first method argument (see A First Look at Classes for more on classes and methods).

### Function: Part 1
Recognise the syntax of function in tutorial 1: `def` and `return`.

### Control flow II:
  - `break`
  - `continue`
  - `pass`

### Generator
  - `yield`
  - search on the diff b/t `range` and `xrange`

- fib_loop.py
- fib_generator.py

### Fibonacci numbers
```
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)
```
Time and space requirement of the following programs
- fib_recusive.py
- fib_dynamic.py
- fib_dynamic2.py

### Python Data Structures
https://docs.python.org/2.7/tutorial/datastructures.html
- Stack and Queue

### A bit more on performance
- counting
- sorting
  - Selection sort
  - Counting sort
  - Merge sort
  - Quick sort

### Python Modules
Guided self study on https://docs.python.org/2.7/tutorial/modules.html
- Play with examples in the above tutorial

### Python File I/O
https://docs.python.org/2.7/tutorial/inputoutput.html
- Play with examples in 7.1 and 7.1.1
  - just to get an idea about how we could format a string in Python
- File I/O
  - Read text from file
  - The CSV data format
  - The JSON data format (JSON, jsonlint)
  - Dump JSON to file

### OOP: Part 1
- [Tutorial](http://anandology.com/python-practice-book/object_oriented_programming.html)
- [OO Concepts](https://www.tutorialspoint.com/python/python_classes_objects.htm)
- Homework: implement 2 classes: Stack and Queue

### Errors and Exceptions
https://docs.python.org/2.7/tutorial/errors.html
- homework: in previous homework, we return special values when the input of
  a function/method is not valid.  Refactor those examples using Errors and Exceptions.

### OOP: Part 2
- Exceptions
- Iterators
- Generators

### Python Standard Library

- [Looping Techniques](https://docs.python.org/2.7/tutorial/datastructures.html#looping-techniques)
- [Standard Library Part 1](https://docs.python.org/2.7/tutorial/stdlib.html)
- [Standard Library Part 2](https://docs.python.org/2.7/tutorial/stdlib2.html)

### Matplotlib Quick Tutorial
Quick example on plotting and drawing a line


### Pandas Quick Tutorial
TODO
