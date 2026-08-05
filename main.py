import datatypes as dt

# ---------------- STRING ----------------

text = input("Enter a String : ")

dt.strm.declaration(text)
dt.strm.indexing(text)
dt.strm.slicing(text)
dt.strm.operations(text)
dt.strm.builtin_functions(text)
dt.strm.comparison(text)

name = input("Enter Name : ")
age = int(input("Enter Age : "))
dt.strm.formatting(name, age)

dt.strm.methods(text)

print("Returned Value :", dt.strm.return_method(text))

# ---------------- LIST ----------------

lst = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    lst.append(num)

print(lst)                                            ##other method to take multiple input               
                                        #lst = list(map(int, input("\nEnter List Elements : ").split()))
dt.lm.creation()
dt.lm.declaration(lst)
dt.lm.indexing(lst)
dt.lm.slicing(lst)
dt.lm.operations(lst)
dt.lm.predefined_functions(lst)
dt.lm.comparison(lst)
dt.lm.methods(lst)
dt.lm.del_operator()
dt.lm.nested_list()

print("Returned List :", dt.lm.return_method(lst))
# ---------------- TUPLE ----------------

#t = tuple(map(int, input("\nEnter Tuple Elements : ").split()))

temp = []

n = int(input("Enter number of tuple elements : "))

for i in range(n):
    temp.append(int(input("Enter element : ")))

t = tuple(temp)

dt.tm.creation()
dt.tm.declaration(t)
dt.tm.indexing(t)
dt.tm.slicing(t)
dt.tm.operations(t)
dt.tm.builtin_functions(t)
dt.tm.comparison(t)
dt.tm.methods(t)
dt.tm.nested_tuple()
dt.tm.list_in_tuple()
dt.tm.packing()
dt.tm.unpacking()

print("Returned Tuple :", dt.tm.return_method(t))

# ---------------- SET ----------------

#s1 = set(map(int, input("\nEnter First Set Elements : ").split()))
#s2 = set(map(int, input("Enter Second Set Elements : ").split()))


s = set()

n = int(input("\nEnter number of set elements : "))

for i in range(n):
    s.add(int(input("Enter element : ")))

s2 = set()

m = int(input("\nEnter number of elements for second set : "))

for i in range(m):
    s2.add(int(input("Enter element : ")))

dt.sm.creation()
dt.sm.declaration(s)
dt.sm.accessing(s)
dt.sm.operations(s, s2)
dt.sm.builtin_functions(s)
dt.sm.comparison(s, s2)
dt.sm.methods(s)
dt.sm.frozen_set()
dt.sm.nested_set()

print("Returned Value :", dt.sm.return_method(s))

# ---------------- DICTIONARY ----------------


d = {}

n = int(input("\nEnter Number of Key-Value Pairs : "))

for i in range(n):
    key = input("Enter Key : ")
    value = input("Enter Value : ")
    d[key] = value


dt.dm.creation()
dt.dm.declaration(d)
dt.dm.accessing(d)
dt.dm.operations(d)
dt.dm.builtin_functions(d)
dt.dm.comparison(d)
dt.dm.methods(d)
dt.dm.del_operator()
dt.dm.nested_dictionary()
dt.dm.list_in_dictionary()
dt.dm.packing()
dt.dm.unpacking()

print("Returned Value :", dt.dm.return_method(d))