Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l =[1,2,3,4]
int(l)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex(l)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    complex(l)
TypeError: complex() first argument must be a string or a number, not 'list'
bool(l)
True
dict(l)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
set(l)
{1, 2, 3, 4}
tuple(l)
(1, 2, 3, 4)
l=['hi' ,[3,4]]
dict(l)
{'h': 'i', 3: 4}
str(l)
"['hi', [3, 4]]"
set(l)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    set(l)
TypeError: unhashable type: 'list'
t=(1 ,2,'hi')
int(t)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
t2=('hi',[3,4],(4,4))
int(t2)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    int(t2)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t2)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    float(t2)
TypeError: float() argument must be a string or a real number, not 'tuple'
bool(t2)
True
dtr(t2)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dtr(t2)
NameError: name 'dtr' is not defined. Did you mean: 'dir'?
str(t2)
"('hi', [3, 4], (4, 4))"
list(t2)
['hi', [3, 4], (4, 4)]
set(t2)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    set(t2)
TypeError: unhashable type: 'list'
dict(t2)
{'h': 'i', 3: 4, 4: 4}
s ={'ho',93,4,(4,4)}
int(s)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(s)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'set'
>>> complex(s)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    complex(s)
TypeError: complex() first argument must be a string or a number, not 'set'
>>> bool(s)
True
>>> d={1:2,'hi':"hello"}
>>> int(d)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
>>> float(d)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'dict'
>>> str(d)
"{1: 2, 'hi': 'hello'}"
>>> list(d)
[1, 'hi']
>>> list(d.items())
[(1, 2), ('hi', 'hello')]
>>> set(d)
{'hi', 1}
>>> tuple(d)
(1, 'hi')
>>> complex(d)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    complex(d)
TypeError: complex() first argument must be a string or a number, not 'dict'
>>> tuple(d.values())
(2, 'hello')
>>> l=[3,5,6.6,True,'hello']
>>> l[3]=55
>>> l
[3, 5, 6.6, 55, 'hello']
>>> n=l
>>> n
[3, 5, 6.6, 55, 'hello']
