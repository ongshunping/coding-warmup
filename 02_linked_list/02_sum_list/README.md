## sum list

Write a function, _sum_list_, that takes in the head of a linked list containing numbers as an argument. The function should return the total sum of all values in the linked list.

#### Test 00
```python
a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)
a.next = b
b.next = c
c.next = d
d.next = e

# 2 -> 8 -> 3 -> -1 -> 7

sum_list(a) # 19`
````
#### Test 01
```python
x = Node(38)
y = Node(4)
x.next = y

# 38 -> 4

sum_list(x) # 42
```

#### Test 02
```python
z = Node(100)

# 100

sum_list(z) # 100
```

#### Test 03
```python
sum_list(None) # 0
```