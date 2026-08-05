# tuple_module.py

# ---------------- TUPLE CREATION (4 TYPES) ----------------

def creation():
    print("\n----- TUPLE CREATION -----")

    t1 = ()                                # Empty tuple
    t2 = (10, 20, 30)                      # Using ()
    t3 = tuple([40, 50, 60])               # Using tuple()
    t4 = (10, "Python", 5.5, True)         # Mixed tuple

    print("Empty Tuple :", t1)
    print("Using () :", t2)
    print("Using tuple() :", t3)
    print("Mixed Tuple :", t4)


# ---------------- DECLARATION ----------------

def declaration(t):
    print("\n----- TUPLE DECLARATION -----")
    print("Tuple :", t)


# ---------------- INDEXING ----------------

def indexing(t):
    print("\n----- TUPLE INDEXING -----")

    print("First Element :", t[0])
    print("Second Element :", t[1])
    print("Last Element :", t[-1])
    print("Second Last Element :", t[-2])


# ---------------- SLICING ----------------

def slicing(t):
    print("\n----- TUPLE SLICING -----")

    print("First 3 Elements :", t[:3])
    print("Last 3 Elements :", t[-3:])
    print("Middle Elements :", t[1:4])
    print("Alternate Elements :", t[::2])
    print("Reverse Tuple :", t[::-1])


# ---------------- OPERATIONS ----------------

def operations(t):

    print("\n----- TUPLE OPERATIONS -----")

    temp = []

    n = int(input("Enter number of elements of second tuple : "))

    for i in range(n):
        temp.append(int(input("Enter element : ")))

    t2 = tuple(temp)

    print("Second Tuple :", t2)

    print("Concatenation :", t + t2)
    print("Repetition :", t * 2)
    print("Membership (10 in tuple) :", 10 in t)
    print("Not Membership (100 not in tuple) :", 100 not in t)


# ---------------- BUILT-IN FUNCTIONS ----------------

def builtin_functions(t):

    print("\n----- BUILT-IN FUNCTIONS -----")

    print("Length :", len(t))
    print("Maximum :", max(t))
    print("Minimum :", min(t))
    print("Sum :", sum(t))
    print("Sorted :", sorted(t))
    print("Type :", type(t))
    print("Any :", any(t))
    print("All :", all(t))
    print("Enumerate :", list(enumerate(t)))
    print("Reversed :", tuple(reversed(t)))
    print("ID :", id(t))


# ---------------- COMPARISON OPERATORS ----------------

def comparison(t):

    print("\n----- COMPARISON OPERATORS -----")

    temp = []

    n = int(input("Enter number of elements of another tuple : "))

    for i in range(n):
        temp.append(int(input("Enter element : ")))

    t2 = tuple(temp)

    print("== :", t == t2)
    print("!= :", t != t2)
    print(">  :", t > t2)
    print("<  :", t < t2)
    print(">= :", t >= t2)
    print("<= :", t <= t2)


# ---------------- TUPLE METHODS ----------------

def methods(t):

    print("\n----- TUPLE METHODS -----")

    print("Count of First Element :", t.count(t[0]))
    print("Index of First Element :", t.index(t[0]))


# ---------------- NESTED TUPLE ----------------

def nested_tuple():

    print("\n----- NESTED TUPLE -----")

    nt = ((10, 20), (30, 40), (50, 60))

    print("Nested Tuple :", nt)
    print("First Tuple :", nt[0])
    print("Second Tuple :", nt[1])
    print("Element :", nt[2][1])


# ---------------- LIST INSIDE TUPLE ----------------

def list_in_tuple():

    print("\n----- LIST INSIDE TUPLE -----")

    t = ([10, 20, 30], [40, 50], ["Python", "Java"])

    print("Tuple :", t)

    print("First List :", t[0])
    print("Second List :", t[1])
    print("Third List :", t[2])

    print("Access Element :", t[0][1])

    t[0].append(100)

    print("After Append :", t)

    t[2][1] = "C++"

    print("After Update :", t)


# ---------------- TUPLE PACKING ----------------

def packing():

    print("\n----- TUPLE PACKING -----")

    t = 10, 20, 30

    print("Packed Tuple :", t)


# ---------------- TUPLE UNPACKING ----------------

def unpacking():

    print("\n----- TUPLE UNPACKING -----")

    t = (100, 200, 300)

    a, b, c = t

    print("a =", a)
    print("b =", b)
    print("c =", c)


# ---------------- RETURN FUNCTION ----------------

def return_method(t):
    return tuple(reversed(t))