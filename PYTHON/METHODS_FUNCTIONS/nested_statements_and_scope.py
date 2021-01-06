#!/usr/bin/python3.6

#LEGB RULES:

#    L : Local - Names assinged in any way within a function (def or lamdba), and not declared global in that function

#    E: Enclosing function locals - Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer

#    G: Global (module) - Names assinged at the top-level of a module file, or declared global in a def within a file.

#    B: Built-in (Python) - Names preassigned in the built-in names module ; open, range, syntax errror

x = 25
def printer():
    x = 50
    return x

print (x)

print (printer())


# Example local

lambda num:num ** 2  # num is local

# Enclosing example, will only print 'Hello Simon'

#GLOBAL
name = 'THIS IS A GLOBAL STRING'

def greet():
    # ENCLOSING
    #name = 'Simon'
    def hello():
        #LOCAL
        #name = 'Terry'
        print ('Hello' + name)
    hello()

greet()

# Exmaple of built in  , eg len command or int or str


x = 50

def func():
    global x # Grabs the value of the global x
    print (f'X is {x}')
    # Local assignment
    x = 200
    b = 5
    print (f' I changed x to : {x}')
    print (locals())

func()

print (x)

print (globals())

print (dir())


