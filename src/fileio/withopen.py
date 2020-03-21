
# # You can do mode="r" or just "r" to use the read
# with open('src/fileio/write.txt', "r") as my_file:
#     print(my_file.readlines())

# with open("src/fileio/write.txt", "r+") as my_file:
#     text = my_file.write("Hey!!!")
#     print(text)  # this print will the num of characters added

# """writing

# You can append, to append to previous work in the file, or write which will overwrite what's already in there

# """
# with open("src/fileio/write.txt", "a") as my_file:
#     text = my_file.write("\n did this delete the other stuff?")
#     print(text)  # this print will the num of characters added

# writing to a file that doesn't exist (yet)

with open("src/fileio/new_file.txt", 'w') as new_file:
    text = new_file.write(
        "Hey, I just wanted to ask if you can read this, too?")

# Keep in mind that you may have to go through a few folders, like above,
# to properly read and write to the file that you actually
# want to use
# you can also use the actual path and start with /user/mainfolder/filefolder/etc
