import sys

# PROGRAM PRE-CONDITIONS

# Check if a file name was provided as a command line argument
if len(sys.argv) < 2:
    print("Please provide a file name as a command line argument.")
    sys.exit(1)

# PROGRAM FUNCTIONS / VARIABLES

# Time Complexity: O(N)
# Input :: FilePath | Output :: [alphanum sequence] list
def tokenize(filePath):
    # Open the file in read mode
  with open(filePath, 'r', encoding='utf-8') as file:
    # Read content in the file
    content = file.read()

    cleaned_text = ""
    for char in content:
        # If the character is alphanumeric, add it to the result
        # Otherwise, add a space
        if char.isalnum():
            cleaned_text += char
        else:
            cleaned_text += ' '

    return list(
      # Turn stripped text string into list without whitespace, and lowercase the result
      map(
        lambda token: token.lower(), 
        cleaned_text.split()
        )
      )

# Time Complexity: O(M)
# Input :: [alphanum] list | Output :: {alphanum: frequency} dictionary
def computeWordFrequencies(wordList):
  word_count = {}
  for word in wordList:
    # Increment the count for each word
    word_count[word] = word_count.get(word, 0) + 1
  return word_count

# Time Complexity: O(K log K)
# Input :: {alphanum: frequency} dictionary | Output :: Command line formatted print of input
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

# Try to tokenize file name and token print frequencies, handle error
try:
    tokens = tokenize(file_name)
    printFrequencies(computeWordFrequencies(tokens))
except FileNotFoundError:
    print(f"The file {file_name} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
