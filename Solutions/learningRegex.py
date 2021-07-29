

import re


str = 'an example word:cat!!'
yah = 'akjfajfih22kaj;lkdjg;aj33'
#match = re.search(r'word:\w\w\w', str)

#If-Statement after search() tests if it succeeded
#if match:
#    print( 'found', match.group()) ## 'found word:cat'
#else:
 #   print('did not find')


#match = re.search(r'\d\d', yah)
#print(match.group())


# re. findall

#mata = re.search(r'iii','piiig')

adf = "sajfajepoieshaadfjkadjf"

#match = re.findall(r"\s", adf)

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

aneeknroy.com

832-561-8861
713.254-3472
713-264-2335

Mr. Roy
Mrs. Robinson
Ms. Jackie
Mr. T
'''

pattern = re.compile(r'\d+\D\d+\D\d+')
#pattern = re.compile(r'\w\w\W')

matches = pattern.finditer(text_to_search)

#for match in matches:
  #  print(match)

txt = 'ajdfka;iet[ignaia[gwinneradjfaoingoiang[ingwinnerafkajdf;iajetnagna[kdgn[a'


matche = re.search(r'[=]',txt)

if matche:
    print(matche.group())





















