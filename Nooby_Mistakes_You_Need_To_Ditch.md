1. Use f strings than manual string format.
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
3. Do not use try-finally
```
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM):
try:
  s.connect((host, port))
  s.sendal(b'hello,world')
finally:
s.close()
```
instead use (most resources that need to be closed have their own context manager,so use it)
```
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((host, port))
  s.sendal(b'hello,world')
```
4. Do nor use bare except keyword
5. Do not use this:
```
def append(n, l=[]):
  l.append(n)
  return l
l1 = append(1) # [1]
l2 = append(2) # [1,2]
```
Use like this:
```
def append(n, l=None):
  if l is None:
    l = []
  l.append(n)
  return l
l1 = append(1) # [1]
l2 = append(2) # [2]
```
