# Kindle-Highlights-Cleanup
Cleanup your Kindle Highlights to be able to export them and summarize them without the limits of the export option.
This script removes highlight metadata lines from a Kindle export based on a specified pattern.

By default it removes the: "Yellow highlight | Location: X Options" metadata lines from the file, that are added when you manually copy-paste.

**Steps**
1. Find the highlights you want here: https://read.amazon.com/notebook
2. Copy manually the ones you want to select.
3. Save them in a highlights.txt file
4. Run `python clean_highlights.py highlights.txt clean.txt`

By default, the pattern recognized is: "Yellow highlight | Location: X".
You can change it for other patterns by calling: `python clean_highlights.py input_file output_file --pattern your_pattern`
