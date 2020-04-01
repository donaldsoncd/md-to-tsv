# open.property

# A script that opens a text file and reads it.

def openFile(file):
    # Use the method open with the parameter "r" to read the contents of a text file
    f = open("sample.md","r")

    # Use the file method "read" to copy the contents of "sample.txt" into the variable "text"
    text = f.read()

    return(text)
