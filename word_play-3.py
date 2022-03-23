# Author: CRS 03/16/22
# Open file and read lines
file = open("words.txt")
lines = file.readline()
def avoid(forbidden_letters):
    acceptable_counter = 0
    for line in file:
        if forbidden_letters not in line:
            acceptable_counter += 1
        break
    print('{0} acceptable words found.'.format(avoid(acceptable_counter)))  

print(avoid(str(input('Enter non acceptable letters: '))))