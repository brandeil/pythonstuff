filename="c:\\users\\len\\documents\\aws_adminwebconsole.txt"

#read entire file at once
with open(filename) as f_obj:
    contents=f_obj.read()

print(contents)

#read file line by line
with open(filename) as f_obj:
    for line in f_obj:
        if line != "\n":
            print(line.rstrip())

#storing the lines in a list
myfile=[]
with open(filename) as f_obj:
    myfile=f_obj.readlines()

print(len(myfile))
print(myfile)        

#writing to a file
with open('somefile','w') as f:
   f.write("mystuff to write")
