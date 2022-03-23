# Author: CRS 03/16/22
# Define function
def number_e():
    # Open words.txt
    with open("words.txt") as infile:
        # Open  words_without_e.txt
        outfile = open("words_without_e.txt", "w")
        # Set variables
        word_count = 0
        words_without_e = 0
        # Create for loops to check for an e
        for l in infile:
            not_e = False
            counter = 0
            word_count += 1
            for letter in l:
                if letter != "e":
                    counter += 1
                    if counter == len(l):
                        words_without_e += 1
                        not_e = True
                        break
            if not_e == True:
                outfile.write(l + "\n")
    # Print the percentage
    percent = (words_without_e / word_count) * 100
    print("Percent of words without e: {0}".format(percent))
# Test the code
number_e()