# Author: CRS 03/16/22
# Define avoid function
def avoid(string,letters):
    # Open file
    with open("words.txt") as infile:
        words_with = 0
        # Create loop to add to counter
        for wordLetter in letters:
            counter = 0 
            found = False
            for letter in string:
                if letter != wordLetter:
                    counter += 1
                    if counter == len(string):
                        found = False
                else:
                    found = True
            if found == True:
                return True
                # Prompt user for forbidden letters
        forbidden_letters = input("Input Letters that you do not want from the txt file: ")
        # Create for loop to check for forbidden letters
        for line in infile:
            counter = 0
            for letter in line:
                if letter != forbidden_letters:
                    counter += 1
                    if counter == len(line):
                        words_with += 1
                        break
# Run code
print(avoid("yep", "yep"))