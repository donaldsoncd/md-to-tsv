# nofootnotes.py

# A script to remove pandoc footnotes from a plaintext file

def stripFoots(text):

    outsideFoot = 1
    noFoot = ""

    for char in text:
        if char == '[':
            outsideFoot = 0
        elif (outsideFoot == 0 and char == '\n'):
            outsideFoot = 1
        elif outsideFoot == 0:
            continue
        else:
            noFoot += char
            continue
    return(noFoot)
