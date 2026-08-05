# string_module.py

# Declaration
def declaration(text):
    print("\n----- STRING DECLARATION -----")
    print("String :", text)


# Indexing
def indexing(text):
    print("\n----- STRING INDEXING -----")
    print("First Character :", text[0])
    print("Last Character :", text[-1])
    print("Second Character :", text[1])
    print("Second Last Character :", text[-2])


# Slicing
def slicing(text):
    print("\n----- STRING SLICING -----")
    print("First 3 Characters :", text[:3])
    print("Last 3 Characters :", text[-3:])
    print("Characters 2 to 5 :", text[1:5])
    print("Alternate Characters :", text[::2])
    print("Reverse String :", text[::-1])


# Operations
def operations(text):
    print("\n----- STRING OPERATIONS -----")
    print("Concatenation :", text + " Python")
    print("Repetition :", text * 2)
    print("Membership ('a' in string):", "a" in text)
    print("Not Membership ('z' not in string):", "z" not in text)


# Built-in Functions
def builtin_functions(text):
    print("\n----- BUILT-IN FUNCTIONS -----")
    print("Length :", len(text))
    print("Maximum Character :", max(text))
    print("Minimum Character :", min(text))
    print("Sorted Characters :", sorted(text))


# Comparison Operators
def comparison(text):
    print("\n----- COMPARISON OPERATORS -----")

    s2 = input("Enter another string for comparison : ")

    print("== :", text == s2)
    print("!= :", text != s2)
    print(">  :", text > s2)
    print("<  :", text < s2)
    print(">= :", text >= s2)
    print("<= :", text <= s2)


# Four Ways of String Formatting
def formatting(name, age):
    print("\n----- STRING FORMATTING -----")

    # 1. Comma Separated
    print("1. Comma :", name, age)

    # 2. % Formatting
    print("2. %% Formatting : Name = %s Age = %d" % (name, age))

    # 3. format()
    print("3. format() : Name = {} Age = {}".format(name, age))

    # 4. f-string
    print(f"4. f-string : Name = {name} Age = {age}")


# String Methods
def methods(text):
    print("\n----- STRING METHODS -----")

    print("Upper :", text.upper())
    print("Lower :", text.lower())
    print("Title :", text.title())
    print("Capitalize :", text.capitalize())
    print("Swapcase :", text.swapcase())
    print("Replace :", text.replace("a", "@"))
    print("Count :", text.count("a"))
    print("Find :", text.find("a"))
    print("Index :", text.index(text[0]))
    print("Startswith :", text.startswith("P"))
    print("Endswith :", text.endswith("n"))
    print("Is Alpha :", text.isalpha())
    print("Is Digit :", text.isdigit())
    print("Is Alnum :", text.isalnum())
    print("Split :", text.split())
    print("Strip :", text.strip())


# Return Type Function
def return_method(text):
    return text[::-1]