# import module sys to get the type of exception
import sys

# Question 1 - Helen of Troy
# open file
# process contents
# close file

# Try helen's file
try:
    pass
except Exception as e:
    print("Oops!", e.__class__, "occurred.")
    print("File does not exist.")
    print()

# write to newly created file
#WRITE TO FILE HERE
print()

# try newly created file
try:
    pass
except Exception as e:
    print("Oops!", e.__class__, "occurred.")
    print("File does not exist.")
    print()



# Question 2 - Process input
random_str = '123$567H3'
#use variable accum for storing the addition of entries
for entry in random_str:
    try:
        pass
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Invalid entries will be ignored.")
        print("Will process next entry.")
        print()
#print("The sum of all number in the entry string is: ", accum)
