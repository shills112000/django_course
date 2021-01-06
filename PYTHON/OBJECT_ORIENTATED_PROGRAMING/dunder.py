#!/usr/local/bin/python3.7

# __   =  double underscore called special methods or magic or dunder

mylist= [1,2,3]
print (len(mylist))

class Sample():
    pass

mysample= Sample()

#len(mysample) # get error as sample has no length currently
print (mysample) # get the object
print (mylist)


class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print (f"A book object has been deleted: {self.title}")

b = Book('Python Rocks', 'Jose', 200)

print (b)  # because print trys to do a string repersentation it uses the __str__ in the class
print (str(b)) # This also calls the __str__ method in the class
print (len(b))

# if you wantd to delete a book

del b # deletes book b
print (b)
