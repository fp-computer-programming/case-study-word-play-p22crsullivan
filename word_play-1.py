# Author: CRS 03/16/22
ofile = open("words.txt", "r+")
new_file = open("greater_than_20.txt", "w")
contents = ofile.readlines()
if len(contents) > 20:
    new_file.write(contents)
ofile.close()
new_file.close()
