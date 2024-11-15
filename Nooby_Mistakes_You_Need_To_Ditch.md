1. use f strings than manual string format.
2. Do not open file like this
```
f = open(filename,"w)
f.write("hello")
f.close()
```
instead use this:
```
with open(filename) as f:
  f.write("hello")
# this will ensure that the file is closed even if the file throws any exception.
```
3. 
