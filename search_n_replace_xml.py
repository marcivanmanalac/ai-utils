import os
import re

# Set the directory containing the XML files
directory = 'path/to/xml/files'

# Set the word to search for and the replacement word
# Note: You need to enclose the search and replace words in quotes
# and use the \b word boundary marker to match the full words
search_word = r'\bold_phrase\b'
replace_word = 'new_phrase'

# Iterate through all the files in the directory
for filename in os.listdir(directory):
  # Check if the file is an XML file
  if filename.endswith('.xml'):
    # Open the file and read its contents
    with open(os.path.join(directory, filename), 'r') as file:
      file_contents = file.read()

    # Replace the search word with the replacement word
    new_contents = re.sub(search_word, replace_word, file_contents)

    # Write the modified contents back to the file
    with open(os.path.join(directory, filename), 'w') as file:
      file.write(new_contents)

print('Done!')
