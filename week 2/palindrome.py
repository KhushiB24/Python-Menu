import Palindrome
def is Palindrome(n): # n is a number, no self argument
    s = str(n)    # convert the number into a string
    r = s[::-1]   # get a reversed copy of the string (as a local variable)
    if (s == r):  # compare them (as before, just with new variable names)
        print "palindrome"