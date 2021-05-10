'''
Characters with more than one meaning:
-           -->  at the beginning/end it means literal dash OR can specify range used in the middle (e.g. 1-5 or a-z)
^           --> beginning of a string OR just negating a set in character set (e.g. [^A-Z], meaning not uppercase letter)


PATTERNS:
.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)


ANCHORS (they do not match any characters but rather invisible positions before/after chatacters):
\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String


CHARACTER SETS:
[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group         --> to match several different patterns (e.g. Mr., Mrs., Ms ...Smith)


QUANTIFIERS (to match more than one character):
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)


Note:
Alphanumericals are a combination of alphabetical and numerical characters,
and is used to describe the collection of Latin letters and Arabic digits 
or a text constructed from this collection.

'''

import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

He HeHe

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

kamhaj@example.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
847-555-1234
900-555-1234
900_555_1234
Mr. Hajdi
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
'''


## raw string (prefixed with 'r' to tell Python not to handle backslashes in any special way)
## e.g. print(r'\tTab') 






''' find every 'abc' '''
# re.complile() - used to separate our patterns into a variable (for reuse/multiple searches)
pattern = re.compile(r'abc')    # note: case sensitive

# variable for matches (finditer returns match objects)
matches = pattern.finditer(text_to_search)      # can use .findall() for pure string matches

# looping through results
# for match in matches:
#     print(match)            # <re.Match object; span=(1, 4), match='abc'>





''' find dots '''
# wrong way: re.compile(r'.') 
# right way:
pattern = re.compile(r'\.') 
matches = pattern.finditer(text_to_search)




''' find my email '''
pattern = re.compile(r'kamhaj@example\.com')    # re.compile(r'kamhaj@example.com')   worked too
matches = pattern.finditer(text_to_search)




''' find many digit between 0 and 9 '''
pattern = re.compile(r'\d') 
matches = pattern.finditer(text_to_search)



''' find based on word boundaries before a word "He" '''
# <re.Match object; span=(67, 69), match='He'>
# <re.Match object; span=(70, 72), match='He'>
pattern = re.compile(r'\bHe')       # would match first and second 'He' in "He Hehe", because third is a middle of a word

# <re.Match object; span=(72, 74), match='He'>
pattern2 = re.compile(r'\BHe')       # would match third 'He' in "He Hehe"

matches = pattern.finditer(text_to_search)



''' find word that is at the beginning (ONLY!) '''
sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'^Start') 
pattern2 = re.compile(r'end$') 
matches = pattern.finditer(sentence)



''' find phone numbers 
321-555-4321
123.555.1234
'''
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') 
matches = pattern.finditer(text_to_search)

# with open('data.txt', 'r', encoding='utf-8') as f:
#     contents = f.read()     # reads all file
# matches = pattern.finditer(contents)


''' find phone numbers, but with specified separators (characterset - square brackets)
321-555-4321
123.555.1234
'''
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d') 
matches = pattern.finditer(text_to_search)


''' find phone numbers, but match only 8xx and 9xx numbers at the beginning
321-555-4321
123.555.1234
'''
pattern = re.compile(r'[89]\d\d[-.]\d\d\d[-.]\d\d\d\d') 
matches = pattern.finditer(text_to_search)



''' find phone numbers, but only match digits between 1 and 5 (dash placed in the middle means range, not literal dash)
321-555-4321
123.555.1234
'''
pattern = re.compile(r'[1-5]') 
matches = pattern.finditer(text_to_search)


''' match every 3-letter word ending with 'at', but not starting with 'b'  '''
# <re.Match object; span=(309, 312), match='cat'>
# <re.Match object; span=(313, 316), match='mat'>
# <re.Match object; span=(317, 320), match='pat'>
pattern = re.compile(r'[^b]at') 
matches = pattern.finditer(text_to_search)


# for match in matches:
#     print(match) 
# print('\n\n\n')