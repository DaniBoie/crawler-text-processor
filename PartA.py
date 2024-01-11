import sys

# PROGRAM FUNCTIONS / VARIABLES

punctuationMarks = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'

def tokenize(filePath):
    # Open the file in read mode
  with open(filePath, 'r', encoding='utf-8') as file:
    # Read content in the file
    content = file.read()
    # translate punctuation marks in content to whitespace
    translation_table = str.maketrans(punctuationMarks, ' ' * len(punctuationMarks))
    stripped_text = content.translate(translation_table)

    return list(
      # Turn stripped text string into list without whitespace, and lowercase the result
      map(
        lambda token: token.lower(), 
        stripped_text.split()
        )
      )

def computeWordFrequencies(wordList):
  word_count = {}
  for word in wordList:
    # Increment the count for each word
    word_count[word] = word_count.get(word, 0) + 1
  return word_count

def printFrequencies(frequencyMap):
  # Sort the dictionary by value (frequency) and then by key (word) in case of ties
  sorted_word_map = sorted(frequencyMap.items(), key=lambda item: (-item[1], item[0]))
    
  # Print the sorted word frequency counts
  for word, count in sorted_word_map:
    print(f"{word}\t{count}")

# MAIN PROGRAM

# Get file name and set up word list
file_name = sys.argv[1]
tokens = [];

# Try to tokenize file name, handle error
try:
    tokens = tokenize(file_name)
finally:
  printFrequencies(computeWordFrequencies(tokens))
