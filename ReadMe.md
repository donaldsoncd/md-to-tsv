# Markdown to Tab Separated Value

I made this "program" to automate part of converting critical edition style text (Jula-English-Arabic plus footnotes for a partial oral interpretation of the Quran into Jula) written using pandoc flavored markdown into a tsv format useful for further analysis as a spreadsheet or data fed int a parallel corpus.

## What the original file looked like

The program assumes that you are producing a trilingual version such as the following:

```
### 3.1.1

Mɔgɔ minnu

_Those people who_

الَّذِينَ

### 3.1.2

olu limaniyara

_believe_

يُؤْمِنُونَ

### 3.2

ni ko dogonin ye[^cba3]

_in hidden affairs_

بِالْغَيْبِ

[^cba3]: SS: religious things not seen such as heaven
```    

## How to use

- Put your text into the file `sample.md`
- Run `cleanup.py`

## Known Issues

If your critical edition uses more than one footnote marker per line (e.g., `A line of text[^1] with two note markers[^2]`) than program will cut off the text following the first footnote marker.

You can resolve this manually if you do not have too many lines with multiple footnotes or you can prepare your text beforehand.

Alternatively, do not use more than one footnote per line.
