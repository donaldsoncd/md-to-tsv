# nofootmark.py

# Create a function to remove footnote markers

def stripFootMark(text):

	outsideFootMark = 1
	noFootMark = ""

	for char in text:
		if char == '[':
			outsideFootMark = 0
		elif (outsideFootMark == 0 and char == ']'):
			outsideFootMark == 1
		elif outsideFootMark == 0:
			continue
		else:
			noFootMark += char
			continue

	noFootMark = noFootMark.replace('[]','')

	return(noFootMark)
