# Author: CRS 03/16/22
# Open the documents
with open("words.txt") as infile, open("greater_than_20.txt", "w") as outfile:
    # Create for loop to determine if a line is greater than 20
    for line in infile.readlines():
        if len(line.strip()) > 20:
            # Write to the new file if the line is greater than 20
            outfile.write(line)