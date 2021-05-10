''' slightly more advanced use of regular expresions

QUANTIFIERS (to match more than one character):
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)

'''
import re
from regex_basics import text_to_search




''' match phone numbers, but using quantifiers '''
pattern = re.compile(r'\d{3}.\d{3}.\d{4}') 
pattern2 = re.compile(r'\d{3}.\d{3}.\d{3,4}') 
matches = pattern.finditer(text_to_search)




''' match names with their different prefixes
Mr. Hajdi
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''
pattern = re.compile(r'Mr\.?\s[A-Z]\w*') 
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)




''' match names with their different prefixes - "Mr." or "Mr" and with one capital letter after space, plus 0 or more letters (\w)
Mr. Hajdi
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''
pattern = re.compile(r'Mr\.?\s[A-Z]\w*') 
matches = pattern.finditer(text_to_search)




''' match names with their different prefixes, including Ms and Mrs. - using GROUPS'''
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*') 
matches = pattern.finditer(text_to_search)


for match in matches:
    print(match)
# output:
# <re.Match object; span=(252, 261), match='Mr. Hajdi'>
# <re.Match object; span=(262, 270), match='Mr Smith'>
# <re.Match object; span=(294, 299), match='Mr. T'>
# <re.Match object; span=(252, 261), match='Mr. Hajdi'>
# <re.Match object; span=(262, 270), match='Mr Smith'>
# <re.Match object; span=(271, 279), match='Ms Davis'>
# <re.Match object; span=(280, 293), match='Mrs. Robinson'>
# <re.Match object; span=(294, 299), match='Mr. T'>





