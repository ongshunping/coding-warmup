## get node value

Write a function, _get_node_value_, that takes in the head of a linked list and an index. The function should return the value of the linked list at the specified index.

If there is no node at the given index, then return _None_.

#### Test 00
```python
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

get_node_value(a, 2) # 'c'
```
#### Test 01
```python
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

get_node_value(a, 3) # 'd'
```
#### Test 02
```python
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

get_node_value(a, 7) # None
```
#### Test 03
```python
node1 = Node("banana")
node2 = Node("mango")
node1.next = node2

# banana -> mango

get_node_value(node1, 0) # 'banana'
```
#### Test 04
```python
node1 = Node("banana")
node2 = Node("mango")
node1.next = node2

# banana -> mango

get_node_value(node1, 1) # 'mango'
```