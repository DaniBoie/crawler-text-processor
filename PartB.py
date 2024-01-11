import sys

# PROGRAM PRE-CONDITIONS

# Check if a file name was provided as a command line argument
if len(sys.argv) < 3:
    print("Please provide 2 file names as a command line argument.")
    sys.exit(1)

# PROGRAM FUNCTIONS / VARIABLES

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

def computeWordFrequencies(wordList):
  word_count = set()
  for word in wordList:
    # Increment the count for each word
    word_count.add(word)
  return word_count

def printFrequencies(set1, set2):
  print(len(set1.intersection(set2)))


# MAIN PROGRAM

# Get file name and set up word list
file_name1 = sys.argv[1]
file_name2 = sys.argv[2]

file_set1 = set();
file_set2 = set();

# Try to tokenize file name and token print frequencies, handle error
try:
    file_set1 = computeWordFrequencies(tokenize(file_name1)) 
except FileNotFoundError:
    print(f"The file {file_name1} does not exist.")
    sys.exit(1)
except Exception as e:
    print(f"An error occurred in file1 processing: {e}")
    sys.exit(1)

# Try to tokenize file name and token print frequencies, handle error
try:
    file_set2 = computeWordFrequencies(tokenize(file_name2)) 
except FileNotFoundError:
    print(f"The file {file_name2} does not exist.")
    sys.exit(1)
except Exception as e:
    print(f"An error occurred in file2 processing: {e}")
    sys.exit(1)

try:
  printFrequencies(file_set1, file_set2)
except e:
  print(f"An error occurred merge file processing: {e}")