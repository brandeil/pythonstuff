# lists
# store sets of mixed data
mylist = []
mylist.append('test')
mylist.append('person')
mylist.sort()
for i in mylist:
    print(i)

# tuples
# a tuple is like a list but you cannot change the values in a tuple once its defined
# however you can override an entire tuple
mytuple=(0,1,2,3,4,5)
print(len(mytuple))

# dictionaries
# key-value pairs
alien_0={'color':'green','points':40}
print(alien_0.get('color','red'))
print(alien_0.get('points',0))
print(alien_0.get('shade'))
alien_0['x']="tbd"
print(alien_0.get('x'))
print("iterate dictionary")
for i in alien_0.keys():
    print(i)

print("Dictionary length is {0}".format(len(alien_0)))

# range of numbers from arg1 to arg2
for i in range(1,5):
    print(i)

# conditional tests with lists
if mylist:  #check if mylist has values
    if 'test' in mylist:
        print("test is there")
    else:
        print("test is not there")
else:
    print("mylist is empty.")

# get type of variable
print("Mylist is of type {0}".format(type(mylist)))

