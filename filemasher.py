import os
import glob

# This was made by a total python noob, i'm storing it on github just so i can keep a record of it myself.
# If anyone wants to improve this PLEASE do because i'd love to see and use a better one.

comment_style = "//"    # change this to the single line comment of your programming language of choice



cwd = os.getcwd()
holder = ""
main = ""
done = 0
while not done:
    print "Please enter the filename which you would like the files to be mashed into..."
    main = raw_input( "Filename: " )
    done = 1

for subdir, dirs, files in os.walk( cwd ):        # loop through files in the dir
    for file in files:
        if file != "filemasher.py" and file != main and file != ".DS_Store":        # make sure we don't read the py script, the mashed file and DS_STORE for mac
            f = open(file, 'r')
            holder = holder + "\n\n" + comment_style + "-------" + file + "-------" + comment_style + "\n\n"  # title for each section
            for line in f.readlines():          # loop through the opened file and add the lines into our holder
                holder = holder + line
            f.close()

FILE = open( main, "w" )        #update the file
FILE.write( holder )
FILE.close()