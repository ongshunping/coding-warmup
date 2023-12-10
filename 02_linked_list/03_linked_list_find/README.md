## linked list find

Write a function, _linked_list_find_, that takes in the head of a linked list and a target value. The function should return a boolean indicating whether or not the linked list contains the target.

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

linked_list_find(a, "c") # True
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

linked_list_find(a, "d") # True
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

linked_list_find(a, "q") # False
```

#### Test 03
```python
node1 = Node("jason")
node2 = Node("leneli")
node1.next = node2

# jason -> leneli

linked_list_find(node1, "jason") # True
```

#### Test 04
```python
node1 = Node(42) # 42

linked_list_find(node1, 42) # True`
```

#### Test 05

```python
node1 = Node(42) # 42

linked_list_find(node1, 100) # False
```






