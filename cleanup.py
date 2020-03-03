# cleanup.py

# A Python program to manipulate the Jula Sura 2 markdown to remove foonotes and put it into a tabular data form

import readmd, nofootnotes, removelines, nofnmarkers

# Create a blank variable "file"
file = ""

# Fill `file` with the contents of `sample.md`
file = readmd.openFile(file)

# Run stripFoots to remove footnotes
file = nofootnotes.stripFoots(file)
print(">>>>>> Here is a sample of the contents without footnotes:\n\nSTART\n\n" + file[1:300] + "\n\nEND\n")

# Run noWhiteLines to remove blank lines

print(">>>>>>> Removing blank lines, header symbols, horizontal line breaks and underscores\n")
file = removelines.noWhiteLines(file)

# Remove header symbols, horizontal line breaks and underscores
file = file.replace('### ','')
file = file.replace('---\n','')
file = file.replace('_','')

print(">>>>>> Here is a sample of the contents without headers etc.:\n\nSTART\n\n" + file[1:300] + "\n\nEND\n")








print(">>>>>>> Saving the cleaned up version")

f = open("new-text.md","w")
f.write(file)
f.close()

print("\nDONE!\n\n")
