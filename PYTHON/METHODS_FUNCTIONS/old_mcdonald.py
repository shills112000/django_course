#!/usr/bin/python3.6

def old_macdonald(name):
    count=0
    new_word=''
    for letter in name:
        if count == 0 or count == 3:
            print (f"count {count}")
            print (f"letter {letter}")
            new_word= new_word + letter.upper()
        else:
            new_word = new_word + letter
        count += 1

    return new_word

# Check
x=old_macdonald('macdonald')
print (x)
