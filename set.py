# user input and display in set 
s1= set()
for val in range(6):
    num = int(input("enter values:"))
    print(num)
    s1.add(num)
    print(s1)

# empty set 
s1={} 
print(s1,type(s1))  # o/p is dict not set

s1= set()
print(s1,type(s1))

# non empty set

a=10
s= set([a])
print(s,type(s))

s= set((a))
print(s,type(s))

s= set((a,))
print(s,type(s))

# Set Functions and Methods in One Program

# Creating sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print("Set 1:", set1)
print("Set 2:", set2)

# add()
set1.add(80)
print("\nAfter add(80):", set1)

# update()
set1.update([90, 100])
print("After update([90,100]):", set1)

# remove()
set1.remove(20)
print("After remove(20):", set1)

# discard()
set1.discard(200)      # No error if element is absent
print("After discard(200):", set1)

# pop()
removed = set1.pop()
print("Popped Element:", removed)
print("After pop():", set1)

# copy()
copy_set = set1.copy()
print("Copy of Set1:", copy_set)

# union()
print("Union:", set1.union(set2))

# intersection()
print("Intersection:", set1.intersection(set2))

# difference()
print("Difference (set1 - set2):", set1.difference(set2))

# symmetric_difference()
print("Symmetric Difference:", set1.symmetric_difference(set2))

# issubset()
print("Is {30,40} subset of set2?", {30, 40}.issubset(set2))

# issuperset()
print("Is set2 superset of {30,40}?", set2.issuperset({30, 40}))

# isdisjoint()
print("Are {1,2} and set2 disjoint?", {1, 2}.isdisjoint(set2))

# clear()
temp = {1, 2, 3}
temp.clear()
print("After clear():", temp)

# len()
print("Length of set1:", len(set1))

# max() and min()
print("Maximum:", max(set2))
print("Minimum:", min(set2))

# sum()
print("Sum:", sum(set2))

# sorted()
print("Sorted set2:", sorted(set2))

# Membership operators
print("30 in set2?", 30 in set2)
print("100 not in set2?", 100 not in set2)