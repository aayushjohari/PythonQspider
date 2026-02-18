Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=[3,4.7, True,'hello',[3,4,5]]
a
[3, 4.7, True, 'hello', [3, 4, 5]]
b=a.copy
b
<built-in method copy of list object at 0x000002ACF1E9D300>
b=a.copy()
b
[3, 4.7, True, 'hello', [3, 4, 5]]
a[1]=7
a
[3, 7, True, 'hello', [3, 4, 5]]
b
[3, 4.7, True, 'hello', [3, 4, 5]]
a[-1][1]=7
a
[3, 7, True, 'hello', [3, 7, 5]]
b
[3, 4.7, True, 'hello', [3, 7, 5]]
import copy
c= copy.deepcopy(a)
c
[3, 7, True, 'hello', [3, 7, 5]]
a[-1][1]=9
c
[3, 7, True, 'hello', [3, 7, 5]]
b
[3, 4.7, True, 'hello', [3, 9, 5]]
a
[3, 7, True, 'hello', [3, 9, 5]]
2+3.1
5.1
2+5+8j
(7+8j)
2+True
3
3+False
3
1+'hello'
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    1+'hello'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
1+[1,2,3]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    1+[1,2,3]
TypeError: unsupported operand type(s) for +: 'int' and 'list'
2.1+3.1
5.2
3.1+5+6j
(8.1+6j)
'hello'+6
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    'hello'+6
TypeError: can only concatenate str (not "int") to str
TypeError: can only concatenate str (not "int") to str
SyntaxError: invalid syntax
a='123'
type(a)
<class 'str'>
int(a)+1
124
'hello'+[1,2,3]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    'hello'+[1,2,3]
TypeError: can only concatenate str (not "list") to str
3-1
2
2-3
-1
2-True
1
'hello'-'hi'
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    'hello'-'hi'
TypeError: unsupported operand type(s) for -: 'str' and 'str'
(1,2,3)-(2,3,4)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    (1,2,3)-(2,3,4)
TypeError: unsupported operand type(s) for -: 'tuple' and 'tuple'
{1,2,3}-{2,3,4}
{1}

[
{a:1,b:2}+{c:1,d:2}
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    {a:1,b:2}+{c:1,d:2}
TypeError: unhashable type: 'list'
1*2
2
>>> 1*5+6j
(5+6j)
>>> 2*5+6j
(10+6j)
>>> 3*(5+6j)
(15+18j)
>>> 2*False
0
>>> 2*'HELLOE'
'HELLOEHELLOE'
>>> 2*[2,3,4]
[2, 3, 4, 2, 3, 4]
>>> 5*[2,3,4]
[2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4]
>>> 2*(2,3)
(2, 3, 2, 3)
>>> 2{2,3}
SyntaxError: invalid syntax
>>> 2*{2,3}
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    2*{2,3}
TypeError: unsupported operand type(s) for *: 'int' and 'set'
>>> {a:1,b:2}*{c:1,d:2}
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    {a:1,b:2}*{c:1,d:2}
TypeError: unhashable type: 'list'
>>> 4.5*6
27.0
>>> 4.5*4+6j
(18+6j)
>>> 4.5*'hello'
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    4.5*'hello'
TypeError: can't multiply sequence by non-int of type 'float'
>>> 3+6j*4+6j
(3+30j)
>>> (3+6j)*True
(3+6j)
>>> True*True
1
>>> True* False
0
