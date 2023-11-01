#- A syntax error occurs when python does not recognize a portion of you cose as valid python code. For example,if  single quote is use
# - defining a string and an apostrophy is used withing that string, the python will interpret the apostrophy as the ending of the string 
# - and try to interpret the remaining string as python code.

message = "One of python's strength is its diverse community"
print(message)

#- The following will give an sytax error 
message = 'One of python's strength is its diverse community'
print(message)