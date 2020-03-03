# removelines.py

# a script that removes blank whitelines in a text file

def noWhiteLines(text):
	text = text.replace('\n\n\n','\n')
	text = text.replace('\n\n','\n')
	return(text)
