import re

pattern = "t"
text = "Does this text match the pattern?"

match = re.search(pattern, text)
s = match.start()
e = match.end()

print('Found "{}"\nin {}\n from {} to {} ("{}")'.format(
    match.re.pattern, match.string, s, e, text[s:e]))
print('-----------------------------')
print(f'Found "{match.re.pattern}"\nin {match.string}\n from {s} to {e} ("{text[s:e]}")')
