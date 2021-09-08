import re

string = "'I AM KELVIN KOH', he said. Though I knew I am true."

print(string)

new = re.sub('[A-Z]', '', string)

print(new)

new = re.sub('[a-z]', '', string)

print(new)

new = re.sub('[.,\'A-Z+" "]', '', string)

print(new)

string = string + "12 344445 - 333"

print(string)

new = re.sub('[^0-9]', '', string)

print(new)
