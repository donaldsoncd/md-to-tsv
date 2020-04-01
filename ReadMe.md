Markdown to Tab Separated Value
==============================

A "program"/"script" to convert a trilingual critical edition style text (that is, a source text with translation into two languages plus annotations/commentary in the form of footnotes) from a plain-text file written using [pandoc](https://pandoc.org/) flavored markdown into an un-annotated tsv useful for further analysis with other software.

How to use
-----------------

Usage:

- Download the python script `to-csv.py`

- Place it the folder along with the annotated text markdown file that you would like to convert to an un-annotated TSV

- Open your terminal and navigate to the folder where the script and your file are

- Run the script by typing in `python to-csv.py` PLUS a list of the languages (e.g., `Jula English Arabic`) with each language separated by a space PLUS the name of your file.

  All together, this means you type something like this, for example:
  
  `python to_csv.py Jula English Arabic text.md`

Markdown formatting specifications
--------------------------------------------------------

   - Each translation unit must start with `###`. 

   - Source language and target language segments are separated by new lines

   - Each translation unit must be have the same number of segments (that is, one for each language) in the same order. (In the above example, that would be English, French, Jula.)

   - Footnotes can be placed at the end of a segment or within a segment (BUT see below for a note on RTL scripts)

   - For instance:

     ```
     ### 1
     
     Hello[^1], this line is in English.[^2]
     
     Bonjour, cette ligne est en français.
     
     I ni ce, nin haya bɛ julakan na.
     
     [^1]: It is interesting that blah blah.
     [^2]: It is worth noting that blah blah.
     ```

Special Notes for Ajami documents and right-to-left scripts such as Arabic
-------------

- Do not place footnotes on any lines written in Arabic script (or a right-to-left script segment, in general) since the mixing of LTR and RTL doesn't work nicely