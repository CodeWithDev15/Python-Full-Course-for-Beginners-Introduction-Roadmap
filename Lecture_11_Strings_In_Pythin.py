name = "Rehbar Khan"
freind = "Veronica"
anotherFriend = "David"

print("Hello", name)

# How you will mentioned someone refer message in Strings?
said = "He said, 'I love you!'"
said_two = 'He said, "I love you!"'
said_three = "She said, \"I love you!\"" # The tick to call refer text is: First Forward Slash then Double quotes then Text then Forward Slash Then Double Quotes
said_four = 'She said, \n\'I love you!\'' # Forward slash n gave you a space\ new line.


# ----------------- # ----------------- # ----------------- # ----------------- # ----------------- # ----------------- # -----------------

# example = "Hello,
# He said:
# How are you?
# "

# Above code example, if you try to print, you will get an EOL error, End Of Line, which means python will not find the with the same line the enclose quote\ character enclose, in order to make multi line string, we will use tripple double or single quotes

o = """Hello!
Example Of Multiple Line String
Why it is useful?
Sometimes we need to print a whole chapter or paragraph
Ot
White paper 
Also it inculde the refer text weather it is single or double quotes
Very cool feature, right
isn't?"""

# Lets learn about index!

# Most of the programming langues start from index 0 and python also starts from an index 0
#We can access string like an array in index.

print(name[0])

# Strings are used when working with unicode characters. What will print at index of three?

# Home Work!

print(name[3]) # Guess the value/output     

# Index out of range error means: When you try access the value out of the range means if it has 5 characters and you are trying to access the postion of six where their does not exsits anything then it gives you an index error.

print(name[10]) # Throws an error.


# I have to consider new line character and also spaces so is their not anthing which gives me the element without mcounting the actual space?

# Looping through the Strings.
# We can loop through the strings using a for lopp like this:

print(name[0]) # I call these also to show the output of this and also the out put of for loop both are the same!
print(name[1])
print(name[2])
print(name[3])
print(name[4])

for chracters in name:
    print(chracters)
