import re

# full string
line = "Apprendre, Le, Python, Scientifique"

print(line)

# split string depending of regex
# '\W+' match anyword occurence in line
# do this 1 time
m = re.split('\W+', line, 1)

# if m is set = true
if m:
    print(m)
else:
    print("No Match!")
