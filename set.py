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
