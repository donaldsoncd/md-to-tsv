# Markdown to Tab Separated Value

A "program"/"script" to convert a critical edition translation text (that is, a source text with translation into one or multiple languages plus annotations/commentary in the form of footnotes) from a plain-text file written using [pandoc](https://pandoc.org/) flavored markdown into an un-annotated tsv useful for further analysis with other software.

## How to use

- Download the python script `to-csv.py`

- Place it the folder along with the annotated text markdown file that you would like to convert to an un-annotated TSV

- Open your terminal and navigate to the folder where the script and your file are

- Run the script by typing in `python to-csv.py` PLUS a list of the languages (e.g., `Jula English Arabic`) with each language separated by a space PLUS the name of your file.

  All together, this means you type something like this, for example:
  
  `python to_csv.py Jula English Arabic text.md`

## Markdown formatting specifications

- Each translation unit must start with `###`. 

- Source language and target language segments are separated by new lines. You can have as many target languages as you want. 

- Each translation unit must be have the same number of segments (that is, one for each language) in the same order.

- Footnotes can be placed at the end of a segment or within a segment (BUT see below for a note on RTL scripts)

- You can place translation segments within underscores (e.g., `_bonjour_`; you may want this markup/formatting for other outputs such Word/LibreOffice docs or HTML files). They will be stripped from the TSV output.


Here's an example of a single translation unit of a text using Jula, English and Arabic:

   ```
   ### 4.2.2
   
   ka na ele[^862c] ma
   
   _and came to you_
   
   إِلَيْكَ
   
   [^862c]: This refers to Muhammad.
   ```

## Special Notes for Ajami documents and right-to-left scripts such as Arabic

- Do not place footnotes on any lines written in Arabic script (or a right-to-left script segment, in general) since the mixing of LTR and RTL doesn't work nicely

## Screenshots

Go from this:

<img width="791" alt="markdown input" src="https://user-images.githubusercontent.com/6858318/78091543-61b2a480-738a-11ea-90eb-0b6323ae83ae.png">

To this:

<img width="698" alt="tsv output" src="https://user-images.githubusercontent.com/6858318/78091554-68411c00-738a-11ea-8e4a-d81fb4b29e1c.png">
