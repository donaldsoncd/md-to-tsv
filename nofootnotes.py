# nofootnotes.py

# A script to remove pandoc footnotes from a plaintext file

# Create a function to remove lines of footnote text
def stripFoots(text):

    outsideFoot = 1
    noFoot = ""

    for char in text:
        if char == '[': # If you hit [ then tell the computer you are inside a footnote
            outsideFoot = 0
        elif (outsideFoot == 0 and char == '\n'): # Otherwise if you are inside a footnote and you hit a new line then tell the computer that it is outside a footnote again
            outsideFoot = 1
        elif outsideFoot == 0: # Otherwise if you are inside a foot then just keep going
            continue
        else: # Otherwise (that is, if you are not inside a footnote then write the character to our new file)
            noFoot += char
            continue
    return(noFoot)
