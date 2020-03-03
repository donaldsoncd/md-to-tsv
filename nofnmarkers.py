# nofnmarkers.py

# A script to remove pandoc foonote markers

def stripFootText(text):

	noFoot = ""

	for line in text:
		if not line.startswith('['):
			noFoot += line
		else:
			continue
	return(text)
