
# List Methods


# 1) `append()`



### Example 1

lst = []
lst.append("Python")
print(lst)



### Example 2

lst.append("Java")
print(lst)


### Example 3

lst.append([23, "Java"])
print(lst)


# 2) `insert()`





### Example 1

lst = [10, 20, 30, 40]
lst.insert(2, "Rs")
print(lst)



### Example 2

lst.insert(-1, 155)
print(lst)

[10, 20, 'Rs', 30, 155, 40]


### Example 3

lst.insert(300, "kop")
print(lst)

[10, 20, 'Rs', 30, 155, 40, 'kop']


### Example 4

lst.insert(-400, 111)
print(lst)

[111, 10, 20, 'Rs', 30, 155, 40, 'kop']


# 3) `remove()`


### Example 1


lst = [10, "Rs", 45.67, 2+3j]
lst.remove("Rs")
print(lst)

[10, 45.67, (2+3j)]

### Example 2

lst.remove(100)
print(lst)



### Example 3

lst.remove(100)

### Example 4

lst.remove(120)

### Example 5

lst = [10, 20, 10, 30, 10]
lst.remove(10)
print(lst)



[20, 10, 30, 10]
