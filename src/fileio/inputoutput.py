# File I/O or, File Input/Output
# Below, we are assigning a variable to the path of the txt file we want to read.
my_file = open('src/fileio/write.txt')

# here we are just using the read method and printing it
print(my_file.read())

# .seek(0) is another way to move the cursor
# .readline() you can continue to call this and move down the lines
# .readlines() will go through and show you each line with the \n new line indicator

# be a kind dev, close the file when you're done
my_file.close()
