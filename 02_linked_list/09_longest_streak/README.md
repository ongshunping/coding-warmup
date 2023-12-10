## longest streak

Write a function, _longest_streak_, that takes in the head of a linked list as an argument. The function should return the length of the longest consecutive streak of the same value within the list.

#### Test 00
```python
a = Node(5)
b = Node(5)
c = Node(7)
d = Node(7)
e = Node(7)
f = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 5 -> 5 -> 7 -> 7 -> 7 -> 6

longest_streak(a) # 3
```
#### Test 01
```python
a = Node(3)
b = Node(3)
c = Node(3)
d = Node(3)
e = Node(9)
f = Node(9)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 3 -> 3 -> 3 -> 3 -> 9 -> 9

longest_streak(a) # 4
```
#### Test 02
```python
a = Node(9)
b = Node(9)
c = Node(1)
d = Node(9)
e = Node(9)
f = Node(9)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 9 -> 9 -> 1 -> 9 -> 9 -> 9

longest_streak(a) # 3
```
#### Test 03
```python
a = Node(5)
b = Node(5)

a.next = b

# 5 -> 5

longest_streak(a) # 2
```
#### Test 04
```python
a = Node(4)

# 4

longest_streak(a) # 1
```
#### Test 05
```python
longest_streak(None) # 0
```