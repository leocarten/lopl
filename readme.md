LOPL stands for Leo's Own Programming Language and can be used to help visualize behind the scene functionality in your code. I created this programming language while reading Crafting Interpreters (https://craftinginterpreters.com). It is a mix of C and JavaScript, but uses the Python Virtual Machine.

A few things about this langauge:
- There are no comments, yet.
- It can perform basic math operations using the `out` command.
- It can vizualize memory locations, bytecode [both high and low level], and can also tell the user the steps taken to declare a variable in this language.

Run this command to install the library: `python3 -m pip install lopl-package`

Create a file structure like this:

```
├── folderName
   ├── interp.py
   ├── code.lopl
```

Open `code.lopl` in a text editor, and write this code:
```
var variable = 10;
viz variable;
h_bytecode variable;
bytecode variable;
out variable * 10;
```

Notice the syntax of the language above. Also, there are a few keywords:

`viz <variableName>`  returns the visualization of a variable declaration.

`h_bytecode <variableName>` returns the high-level bytecode of a variable declaration.

`bytecode <variableName>` returns the true bytecode of a variable declaration.
`out <variableName>` will print out variables. 

**Only `out` can perform mathematical operations in this language.**

`var number = 5 + 5;` does ***NOT*** work.

```
var number = 5;
out number + 5;
```
Will work, and will print `10`.



Open `interp.py` in a text editor, and write this code:
```
from lopl_package import vizualizer
def readFile(input_file):
    with open(input_file, 'r') as file:
        content = file.read()
        return content
    
def readInput(string):
    array = string.split("\n")
    for index, line in enumerate(array):
        vizualizer.evaluate(line, index)  

def main():
    file = readFile("code.lopl")
    readInput(file)

main()
```
