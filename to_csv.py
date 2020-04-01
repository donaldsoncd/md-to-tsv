#!/usr/bin/env python3
help_text = """
Convert from markdown to a tsv of translations.

Usage:

    to_csv [language_name...] filename

    language_name: a space separated list of languages where each value
                   represents language of translation

    filename: the input markdown file to process

    Example:

        to_csv Jula English Arabic crit_units.md

input file notes:
    - Each entry header must start with a ###
    - Translations are separated by new lines
    - Each entry must have the same number of translations in the same order
    - Each entry must have a language name passed in when running the script
"""

import os
import re
import sys

###
# Check if we are running at least Python 3, if not exit with an error
###
if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

###
# check if --help was requested
###
if len(sys.argv) == 2 and sys.argv[1] == "--help":
    print(help_text)
    sys.exit()

##
# Handle command line arguments
##

# The filename of the file to work on must come last
filename = sys.argv.pop()

# The list of language names is everything after the 1st argument.
# The first argument is always the name of the script. This is a UNIX standard.
languages = sys.argv[1:]

# Check to make sure at least one language name was passed in, otherwise
# exit with an error.
if len(languages) < 1 :
    raise Exception("You must specify at least one language.")

##
# Utility functions
##

# Abstract away the functionality of writing a line to the output
# so we can ignore how it actually happens and just call write_line 
def write_line(destination, line):
    destination.append(line)

# Abstract away turning the output into a string for writing and debugging
def to_string(output):
    return "\n".join(output)

# Abstract away saving the file so we can handle it by itself
# We want to save the processed file in the same directory as the input file
# so we must take that as an argument
def save_to_file(data, input_filename):
    # Convert the data to a string
    contents = to_string(data)
    # Get the directory and filename from the input filename
    (directory, file_and_ext) = os.path.split(input_filename)
    # Get the filename minus the extension (.md)
    (output_filename, _) = os.path.splitext(file_and_ext)
    # Build the new complete file name to save to
    output_filename = os.path.join(directory, output_filename + ".tsv")
    # If that file already exists we need to ask to override it
    if os.path.exists(output_filename):
        response = input("The file " + output_filename + " already exists. Overwrite? y/n \n")
        if response.lower() == 'y':
            # If they responded y then write the file 
            do_write_file(contents, output_filename)
        else:
            # If they responded anything else exit
            print("Did not write the file")
    else:
      # If the file doesn't already exist then write the file
      do_write_file(contents, output_filename)

# The actual work of writing the file so we don't have to write it twice
def do_write_file(contents, output_filename):
    with open(output_filename, 'w') as file:
        file.write(contents)
        print("Wrote TSV to: ", output_filename)

# Abstract exiting on error
def error(text):
    print("ERROR:")
    print(text)
    sys.exit(1)

##
# Start processing the input
##

# Create buffer for output
output = []

# Write Header line
header = "ID"
for lang in languages:
    header += "\t" + lang
    
write_line(output, header)


# Store which language we're expecting to run into.
# If the index is len(languages), we're expecting to run into a section header
# If the index is < len(languages) we're expecting to run into a translation
current_language_index = len(languages)

# Store which line number we're working on for good error reporting
line_number = 0

# Store whether we've found the first header
# We ignore everything up til the first header so we need to store if
# we've seen one yet.
found_first_header = False

# Open the input file for reading
with open(filename, 'r') as input_file:
    # Create a buffer for the next line of the CSV file
    next_line = ""
    for line in input_file:
        # Increment the current line_number for good error reporting
        line_number += 1
        # Check if the line is a header line and save the match
        header_match = re.match(r"^###(.*)$", line)
        # If it is a header line...
        if header_match:
            # We've found a header so let's remember that
            found_first_header = True
            # If the next line buffer has any content, write it cos we're done with that line
            if len(next_line) > 0: write_line(output, next_line)
            # If we've seen each language, then we're ready for another header
            if current_language_index == len(languages):
                # Because we've found a header, it's time to start a new line
                next_line = header_match.group(1).strip()
                # The next language we're looking for is the 1st
                current_language_index = 0
            # If we haven't seen each language, but the line matches a header
            # that's an error
            else:
                error("Found a line header but wasn't expecting one at line: " + str(line_number))
        # If we haven't found a header yet, then ignore the line completely
        elif not found_first_header:
            continue
        # If the line is empty or only white space, ignore it
        elif line.strip() == "":
            continue
        # If the line starts with some special chars, ignore them
        elif line.startswith("[") or line.startswith("-"):
            continue
        # If the line looks like an entry, but we've run out of languages
        # that's an error
        elif current_language_index >= len(languages):
            error("Expected a header but found a translation at line: " + str(line_number))
        # If we get here then we're ready to add a language entry to the line
        else:
            # First we remove all white space, then leading and trailing underscores
            processed_line = line.strip().strip('_')
            # Then we remove all footnote entries
            processed_line = re.sub('\[\^.*\]', '', processed_line)
            # Then we add it to the new line
            next_line += '\t' + processed_line
            # We need to increment which language we're expecting so we can know
            # if we're still looking for a language
            current_language_index += 1


    # Try to save the file
    save_to_file(output, filename)
