s = "should string be?!?!"
# Length shuld be 20
print("Length of s = %d" % len(s))

# First occurrence of "t" should be at index 8
print("The first occurrence of the letter t = %d" % s.index("t"))

# Number of s's should be 2
print("s occurs %d times" % s.count("s"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("sho"):
    print("String starts with 'sho'. Good!")

# Check how a string ends
if s.endswith("?!?!"):
    print("String ends with '?!?!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))
