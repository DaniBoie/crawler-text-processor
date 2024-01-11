import sys

punctuationMarks = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'

def tokenize(filePath):
    # Open the file in read mode
  with open(filePath, 'r') as file:
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

# Check if a file name was provided as a command line argument
if len(sys.argv) < 2:
    print("Please provide a file name as a command line argument.")
    sys.exit(1)

file_name = sys.argv[1]
tokens = [];

try:
    tokens = tokenize(file_name)
except FileNotFoundError:
    print(f"The file {file_name} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

printFrequencies(computeWordFrequencies(tokens))
