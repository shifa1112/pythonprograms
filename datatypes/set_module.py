# set_module.py

# ---------------- SET CREATION (4 TYPES) ----------------

def creation():
    print("\n----- SET CREATION -----")

    s1 = set()                          # Empty set
    s2 = {10, 20, 30}                   # Using {}
    s3 = set([40, 50, 60])              # Using set()
    s4 = {10, "Python", 5.5, True}      # Mixed set

    print("Empty Set :", s1)
    print("Using {} :", s2)
    print("Using set() :", s3)
    print("Mixed Set :", s4)


# ---------------- DECLARATION ----------------

def declaration(s):
    print("\n----- SET DECLARATION -----")
    print("Set :", s)


# ---------------- ACCESSING ----------------

def accessing(s):
    print("\n----- ACCESSING SET -----")

    print("Elements are :")
    for i in s:
        print(i, end=" ")
    print()


# ---------------- SET OPERATIONS ----------------

def operations(s):

    print("\n----- SET OPERATIONS -----")

    temp = []

    n = int(input("Enter number of elements for second set : "))

    for i in range(n):
        temp.append(int(input("Enter element : ")))

    s2 = set(temp)

    print("Second Set :", s2)

    print("Union :", s | s2)
    print("Intersection :", s & s2)
    print("Difference :", s - s2)
    print("Symmetric Difference :", s ^ s2)

    print("Membership (10 in set) :", 10 in s)
    print("Not Membership (100 not in set) :", 100 not in s)


# ---------------- BUILT-IN FUNCTIONS ----------------

def builtin_functions(s):

    print("\n----- BUILT-IN FUNCTIONS -----")

    print("Length :", len(s))
    print("Maximum :", max(s))
    print("Minimum :", min(s))
    print("Sum :", sum(s))
    print("Sorted :", sorted(s))
    print("Type :", type(s))
    print("Any :", any(s))
    print("All :", all(s))
    print("Enumerate :", list(enumerate(s)))
    print("ID :", id(s))


# ---------------- COMPARISON OPERATORS ----------------

def comparison(s):

    print("\n----- COMPARISON OPERATORS -----")

    temp = []

    n = int(input("Enter number of elements for another set : "))

    for i in range(n):
        temp.append(int(input("Enter element : ")))

    s2 = set(temp)

    print("== :", s == s2)
    print("!= :", s != s2)
    print(">  :", s > s2)
    print("<  :", s < s2)
    print(">= :", s >= s2)
    print("<= :", s <= s2)


# ---------------- SET METHODS ----------------

def methods(s):

    print("\n----- SET METHODS -----")

    temp = s.copy()

    temp.add(100)
    print("add() :", temp)

    temp.update({200, 300})
    print("update() :", temp)

    temp.remove(100)
    print("remove() :", temp)

    temp.discard(200)
    print("discard() :", temp)

    x = temp.pop()
    print("pop() removed :", x)
    print("After pop :", temp)

    copy_set = temp.copy()
    print("copy() :", copy_set)

    copy_set.clear()
    print("clear() :", copy_set)


# ---------------- FROZENSET ----------------

def frozen_set():

    print("\n----- FROZENSET -----")

    fs = frozenset([10, 20, 30])

    print("Frozen Set :", fs)


# ---------------- NESTED SET ----------------

def nested_set():

    print("\n----- NESTED SET -----")

    s = {frozenset({1, 2}), frozenset({3, 4})}

    print("Nested Set :", s)


# ---------------- RETURN FUNCTION ----------------

def return_method(s):
    return sorted(s)