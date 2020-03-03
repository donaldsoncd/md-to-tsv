# cleanup.py

# A Python program to manipulate the Jula Sura 2 markdown to remove foonotes and put it into a tabular data form

import readmd, nofootnotes

# Create a blank variable "file"
print(">>>>>> Create a blank file")
file = ""
file = readmd.openFile(file)

print(">>>>> Printing the first 50 of the file:" + file[0:50])

# create a variable with the
print(">>>>>> Create a variable by running the function openFile on file:")
file = readmd.openFile(file)

print(">>>>>> Here are the first 100 characters of \"file:" + "\n" + file[0:100])

# Run stripFoots to remove foonotes
print(">>>>>> Run the stripFoots function on \"file\"")
file = nofootnotes.stripFoots(file)

print(">>>>>> Here are the contents without foonotes:\n" + file)

print(">>>>>>> Saving the cleaned up version without footnotes...")

f = open("new-text.md","w")
f.write(file)
f.close()

print("\nDONE!")