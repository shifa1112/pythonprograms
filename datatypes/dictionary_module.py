# dictionary_module.py


# ---------------- DICTIONARY CREATION (4 TYPES) ----------------

def creation():
    print("\n----- DICTIONARY CREATION -----")

    d1 = {}                                      # Empty Dictionary
    d2 = {"Name": "Shifa", "Age": 21}             # Using {}
    d3 = dict(Name="Python", Version=3)           # Using dict()
    d4 = {1: "Java", 2: "Python", 3: "C++"}       # Integer Keys

    print("Empty Dictionary :", d1)
    print("Using {} :", d2)
    print("Using dict() :", d3)
    print("Integer Key Dictionary :", d4)



# ---------------- DECLARATION ----------------

def declaration(d):
    print("\n----- DICTIONARY DECLARATION -----")
    print("Dictionary :", d)



# ---------------- ACCESSING ----------------

def accessing(d):
    print("\n----- DICTIONARY ACCESSING -----")

    key = input("Enter key to access value : ")

    if key in d:
        print("Value :", d[key])
    else:
        print("Key not found")

    print("Keys :", d.keys())
    print("Values :", d.values())
    print("Items :", d.items())



# ---------------- OPERATIONS ----------------

def operations(d):

    print("\n----- DICTIONARY OPERATIONS -----")

    d2 = {}

    n = int(input("Enter number of elements for second dictionary : "))

    for i in range(n):
        key = input("Enter Key : ")
        value = input("Enter Value : ")
        d2[key] = value


    print("Second Dictionary :", d2)

    print("Concatenation using update :")

    temp = d.copy()
    temp.update(d2)

    print(temp)

    print("Membership Key :", "Name" in d)
    print("Not Membership :", "City" not in d)



# ---------------- BUILT-IN FUNCTIONS ----------------

def builtin_functions(d):

    print("\n----- BUILT-IN FUNCTIONS -----")

    print("Length :", len(d))
    print("Type :", type(d))
    print("Keys :", list(d.keys()))
    print("Values :", list(d.values()))
    print("Items :", list(d.items()))
    print("ID :", id(d))
    print("Sorted Keys :", sorted(d))
    print("All :", all(d))
    print("Any :", any(d))



# ---------------- COMPARISON OPERATORS ----------------

def comparison(d):

    print("\n----- COMPARISON OPERATORS -----")

    d2 = {}

    n = int(input("Enter number of elements for another dictionary : "))

    for i in range(n):
        key = input("Enter Key : ")
        value = input("Enter Value : ")
        d2[key] = value


    print("== :", d == d2)
    print("!= :", d != d2)



# ---------------- DICTIONARY METHODS ----------------

def methods(d):

    print("\n----- DICTIONARY METHODS -----")

    temp = d.copy()

    print("Copy :", temp)

    print("Get :", temp.get(list(temp.keys())[0]))

    temp.update({"City": "Kolhapur"})
    print("Update :", temp)

    print("Keys :", temp.keys())

    print("Values :", temp.values())

    print("Items :", temp.items())


    temp.pop("City")
    print("Pop :", temp)


    temp.setdefault("Country", "India")
    print("Setdefault :", temp)


    removed = temp.popitem()
    print("Popitem :", removed)

    print("After Popitem :", temp)



# ---------------- DEL OPERATOR ----------------

def del_operator():

    print("\n----- DEL OPERATOR -----")

    d = {
        "Name": "Python",
        "Version": 3,
        "Year": 1991
    }

    print("Original :", d)

    del d["Year"]

    print("After deleting key :", d)



# ---------------- NESTED DICTIONARY ----------------

def nested_dictionary():

    print("\n----- NESTED DICTIONARY -----")


    student = {

        "Student1":
        {
            "Name": "Shifa",
            "Marks": 90
        },

        "Student2":
        {
            "Name": "Ali",
            "Marks": 85
        }
    }


    print("Nested Dictionary :", student)

    print("Student1 Name :", student["Student1"]["Name"])



# ---------------- LIST INSIDE DICTIONARY ----------------

def list_in_dictionary():

    print("\n----- LIST INSIDE DICTIONARY -----")


    d = {

        "Languages":
        [
            "Python",
            "Java",
            "C++"
        ],

        "Marks":
        [
            90,
            85,
            95
        ]
    }


    print(d)

    print("First Language :", d["Languages"][0])



# ---------------- DICTIONARY PACKING ----------------

def packing():

    print("\n----- DICTIONARY PACKING -----")

    d = dict(Name="Python", Type="Programming")

    print("Packed Dictionary :", d)



# ---------------- DICTIONARY UNPACKING ----------------

def unpacking():

    print("\n----- DICTIONARY UNPACKING -----")

    d = {
        "Name": "Python",
        "Version": 3
    }


    name = d["Name"]
    version = d["Version"]

    print("Name :", name)
    print("Version :", version)



# ---------------- RETURN FUNCTION ----------------

def return_method(d):
    return list(d.keys())