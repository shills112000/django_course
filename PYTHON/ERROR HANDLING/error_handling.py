# Try : This is the block of code to attempt
# Except: Blodk of code will execute iin case there is an error
# Finally: A final block of code to be executed regardless of error

def add (n1,n2):
    
    try:
        print (n1+n2)
    except:
        print ("Cant do it silly")
        
add(10,20)

number1 = 10
#number2 = input("please provide number:")
#add(number1,number2)


try:
    # WANT TO ATTEMPT THIS CODE
    # MAY HAVE AN ERROR
    result= 10 + '10'   # cannot add sting to integer
except:
    # HAPPEN IF ERROR
    print ("hey looks like you arnent adding correctly")
else: 
    print ("all went well")

# use finally

try:
    f= open('test', 'r')
    f.write("test line")
except TypeError:
    print ("there was a type error")
except OSError:
    print ("hey you have an OS error") 
except:
    print ("All other exceptions")
finally:
    print ("I always run")


def ask_for_int():
    while True:
        try:
            result=int(input("Please provide nunber: "))
        except:
            print ("That's not a number")
            continue
        else:
            print (f"number is : {result}")
            break
        finally:
            print ("Not a number, try again")
            print ("I will always run at the end")

ask_for_int()




   