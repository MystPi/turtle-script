# turtle-script
A simple scripting language to draw pictures with Python's Turtle module, made with [Lark](https://github.com/lark-parser/lark).

## Example
```
// Draws a red square
color red
fill {
    f 100
    r 90
}
```
## Commands
```
f [number]                      Move forward [number] steps
b [number]                      Move backward [number] steps
r [number]                      Turn right [number] degrees
l [number]                      Turn left [number degrees
u                               Pen up
d                               Pen down
h                               Hide
s                               Show
fill { [commands] }             Start fill, execute [commands], then end fill
repeat [number] { [commands] }  Execute [commands] [number] times

// Single line comment
/* Multi line comment */
```
## Usage
```python
import turtleScript
turtleScript.run('f 100')
```
