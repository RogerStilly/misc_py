## Program name: sort_fruits.py
## UoPeople CS-1101 December 2015
## Unit 7
## Roger Stillick Jr.
## The purpose of this program is to read a file containing a list of
## fruits, then sort the list and write the sorted list to a new file.


# Set the working directory of the path
wd = '/home/roger/bin/'

#courtesy prompt
print ('Program started')

# open the files to read and write
infile = open(wd + 'unsorted_fruits.txt', 'r')
outfile = open(wd + 'sorted_fruits.txt', 'w')

# the readlines() method is commented out, because I wanted to try
# a different way to accomplish the same task.  It works, so I left it. 
#fruit = infile.readlines()
fruit = list(infile)

#sort the list
fruit.sort()

# iterate over the list "fruit", and write the line to "outfile" if the
# line is not blank. The instructors YouTube example was helpful in
# figuring out how to remove the blank lines.
for line in fruit:
    if line > "/n":
        outfile.write(line)

# don't forget to close the file operations!
infile.close()
outfile.close()

#courtesy prompt
print('''Operation successful, look for the "sorted_fruits.txt" file in
your working directory.''') 
