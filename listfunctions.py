
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




### Example 3

lst.insert(300, "kop")
print(lst)



### Example 4

lst.insert(-400, 111)
print(lst)



# 3) `remove()`


### Example 1


lst = [10, "Rs", 45.67, 2+3j]
lst.remove("Rs")
print(lst)



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

## 4) `pop(index)`

### Definition




lst = [10, 20, 30, 40, 10]

lst.pop(-4)



lst.pop(14)
print(lst)


## 5) `pop()`

### Definition
list.pop()

lst = [10, 20, 30, 40]
print(lst)

lst = []
lst.pop()

IndexError

## 6) `clear()`

### Definition


### Examples




lst = [10, 20, 30, 40, 10]

lst.clear()
print(lst)





[].clear()

None




print([].clear())


## 7) `index()`

### Definition


### Examples

lst = [10, "Bs", 45.67, "Python", 23, True, "High"]

lst.index("Python")



#2

lst.index(23.45)
