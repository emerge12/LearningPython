# - A string is  series of character. Anyhtin inside quotes is considered a string in python
# - Single are double quote can be used around a string. This flexibility allows you to used quotes and apostrophes
simple_message = 'I told my friend "Python is my favorite programming language!"'
print(simple_message)
name = "ADA lovelace"
print(name.title())
print(name.upper())
first_name = "Junior"
last_name = " Sterling"
# - The 'f' in the following code stands for format and thes string are f-strings
full_name = f"{first_name}{last_name}"
print(full_name.title())

# - f-strings can be used to compose full sentense as follow
first_name = "junior"
last_name = " sterling"
full_name = f"{first_name}{last_name}"
print(f"Hello, {full_name.title()}!")


# - f-string can also be used to compose a message and who message is assigned as a variable
first_name = "junior"
last_name = " sterling"
full_name = f"{first_name}{last_name}"
message = f"Hello, {full_name.title()}! How are you?"
print(message)


# - Removing white spaces from string
fav_language = "python "
print(fav_language)
# Using the rstrip() functio this only remove the strip for this execution, however, subsequent call to fav_language variable will include the space
print(fav_language.rstrip())

# To permanently remove space, the strip  value have to be reassigned to the variable as shown below
# -rstrip: Remove white space from the right side of the word
# -lstrip: Remove white space from the left side of the word
# -strip: Remove white space from the both sides of the word

fav_language = fav_language.rstrip()
print(fav_language)

 