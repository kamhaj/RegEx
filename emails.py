import re

emails = '''
KamSHaj@gmail.com
kam.haj@university.edu
kam-321-haj@my-work.net
'''


## write regex that will match different email types
## we can also get ready regex for emails from the internet and it should work just fine
pattern = re.compile(r'[a-zA-z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
pattern_found_online = re.compile(r'[a-zA-z0-9_.+-]+@[a-zA-z0-9-]+\.[a-zA-z0-9-.]+')
matches = pattern_found_online.finditer(emails)

for match in matches:
    print(match)

# output:
# <re.Match object; span=(1, 18), match='KamSHaj@gmail.com'>
# <re.Match object; span=(19, 41), match='kam.haj@university.edu'>
# <re.Match object; span=(42, 65), match='kam-321-haj@my-work.net'>