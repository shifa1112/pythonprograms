# list_module.py

# ---------------- LIST CREATION (4 TYPES) ----------------

def creation():
    print("\n----- LIST CREATION -----")

    l1 = []                              # Empty List
    l2 = [10, 20, 30]                    # Using []
    l3 = list((40, 50, 60))              # Using list()
    l4 = [1, "Python", 5.5, True]        # Mixed List

    print("Empty List :", l1)
    print("Using [] :", l2)
    print("Using list() :", l3)
    print("Mixed List :", l4)


# ---------------- DECLARATION ----------------

def declaration(lst):
    print("\n----- LIST DECLARATION -----")
    print(lst)


# ---------------- INDEXING ----------------

def indexing(lst):
    print("\n----- LIST INDEXING -----")
    print("First :", lst[0])
    print("Last :", lst[-1])
    print("Second :", lst[1])
    print("Second Last :", lst[-2])


# ---------------- SLICING ----------------

def slicing(lst):
    print("\n----- LIST SLICING -----")
    print("First 3 :", lst[:3])
    print("Last 3 :", lst[-3:])
    print("Middle :", lst[1:4])
    print("Alternate :", lst[::2])
    print("Reverse :", lst[::-1])


# ---------------- OPERATIONS ----------------

def operations(lst):
    print("\n----- LIST OPERATIONS -----")

    lst2 = list(map(int, input("Enter another list : ").split()))

    print("Concatenation :", lst + lst2)
    print("Repetition :", lst * 2)
    print("Membership :", 10 in lst)
    print("Not Membership :", 100 not in lst)


# ---------------- PREDEFINED FUNCTIONS ----------------

def predefined_functions(lst):
    print("\n----- PREDEFINED FUNCTIONS -----")

    print("Length :", len(lst))
    print("Maximum :", max(lst))
    print("Minimum :", min(lst))
    print("Sum :", sum(lst))
    print("Sorted :", sorted(lst))
    print("Type :", type(lst))
    print("Any :", any(lst))
    print("All :", all(lst))
    print("Enumerate :", list(enumerate(lst)))
    print("Reversed :", list(reversed(lst)))
    print("Slice :", lst[:])
    print("List Conversion :", list(tuple(lst)))
    print("ID :", id(lst))


# ---------------- COMPARISON ----------------

def comparison(lst):
    print("\n----- COMPARISON OPERATORS -----")

    lst2 = list(map(int, input("Enter another list : ").split()))

    print("==", lst == lst2)
    print("!=", lst != lst2)
    print(">", lst > lst2)
    print("<", lst < lst2)
    print(">=", lst >= lst2)
    print("<=", lst <= lst2)


# ---------------- LIST METHODS ----------------

def methods(lst):
    print("\n----- LIST METHODS -----")

    temp = lst.copy()

    temp.append(100)
    print("Append :", temp)

    temp.extend([200, 300])
    print("Extend :", temp)

    temp.insert(1, 999)
    print("Insert :", temp)

    temp.remove(999)
    print("Remove :", temp)

    temp.pop()
    print("Pop :", temp)

    print("Count :", temp.count(temp[0]))

    print("Index :", temp.index(temp[0]))

    temp.sort()
    print("Sort :", temp)

    temp.reverse()
    print("Reverse :", temp)


# ---------------- DEL OPERATOR ----------------

def del_operator():
    print("\n----- DEL OPERATOR -----")

    l = [10, 20, 30, 40, 50]

    print("Original :", l)

    del l[2]
    print("Delete Element :", l)

    del l[1:3]
    print("Delete Slice :", l)

    del l
    print("Entire List Deleted")


# ---------------- NESTED LIST ----------------

def nested_list():
    print("\n----- NESTED LIST -----")

    n1 = [[1, 2], [3, 4]]
    n2 = [["A", "B"], ["C", "D"]]
    n3 = [[10, 20], ["Python", "Java"]]

    print("Nested List 1 :", n1)
    print("Nested List 2 :", n2)
    print("Mixed Nested List :", n3)

    print("First Element :", n1[0])
    print("Access 4 :", n1[1][1])


# ---------------- RETURN FUNCTION ----------------

def return_method(lst):
    return sorted(lst)