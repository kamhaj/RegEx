import re

urls = '''
https://www.google.com
http://abcdefg.com
https://youtube.com
https://www.nasa.gov
'''

''' match inconsistent url patterns and get DOMAIN NAME and TOP LEVEL DOMAIN (like .com)'''
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')  # we have three groups () here
matches = pattern.finditer(urls)

# for match in matches:
#     print(match.group(3))


## group(0) output:
# https://www.google.com
# http://abcdefg.com
# https://youtube.com
# https://www.nasa.gov

## group(1) output:
# www.
# None
# None
# www.

## group(2) output:
# google
# abcdefg
# youtube
# nasa

## group(3) output:
# .com
# .com
# .com
# .gov


''' get subbed urls using group IDs (e.g. for reformatting text)'''
subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)
# output:
# google.com
# abcdefg.com
# youtube.com
# nasa.gov