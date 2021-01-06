#!/usr/local/bin/python3.7

# using basic.txt

myfile = open('basic.txt')

# Errno 2 : This is when you have the wrong filename or dir
print (type(myfile)) # <class '_io.TextIOWrapper'>
print (myfile) # <_io.TextIOWrapper name='basic.txt' mode='r' encoding='UTF-8'>

print (myfile.read()) # print out the contents of the file # print out the contents of the file


print (myfile.read()) # If you read it again you get nothing as you are already at the bottom of the file

myfile.seek(0) # This goes back to the top of the file
print (myfile.read()) # If you read it again you get nothing as you are already at the bottom of the file


myfile.seek(0) # This goes back to the top of the file
contents=myfile.read() # store the contents of the file into a string
print (type(contents))

myfile.seek(0) # This goes back to the top of the file
print (myfile.readlines()) # This prints a list of the file breaking a newline
myfile.close() # close the file

with open ('basic.txt') as my_new_file:  # put the contents in
    contents = my_new_file.read()
    print (f"\ncontents of file :\n{contents}")


with open ('basic.txt', mode='r') as myfile:  #  mode r is read
    contents= myfile.read()
    print (contents)

## modes
# mode = 'r' read only
# mode = 'w' write only (will overwrite files or create new)
# mode = 'a' append only (add to bottom of file
# mode = 'r+' read and write
# mode = 'w' is writing a reading (overwrites exiting files or creates new file)

with open ('test.txt', mode='r') as f:  #  mode r is read
    print (f.read())


with open ('test.txt', mode='a') as f:  #  mode a is append
    f.write('FOUR ON FOURTH\n')


with open ('write.txt', mode='w') as f:  #  mode w is write
    f.write('I CREATED THIS FILE\n')

