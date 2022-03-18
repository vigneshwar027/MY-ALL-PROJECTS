#import re
# re.keyword('model word','the string in which the operation to be done')
# but while you assign the model word into a variable the format is (a=r'vicky)

# find and replace syntax
# (re.sub('find word','replace word','the sentence in which the changes to be done'))

# note: if model word is avodha it does the operation for avodha
#     whereas if model word is avo... it does the operation for avo(xxx)
#     (where x can be any character)

# character class
#     this method checks the to be checked string
#     with as per the defined model string letter by letter





#example below

import re

if re.match('[0-9][A-Z][a-z]','9ACz'):#checkks only the 1st three letters defined
    print('letter sequence match')
else:
    print('letter sequence do not match')




print(re.findall('vicky','the good boydfsff is vicky andfsdjsdj vickyfsdf is a good boy'))
if re.match('vi.ky','visky the good boy is vicky and vicky is a good boy'):
    print('string matches')
else:
    print('string not matches')


if (re.search('vicky','vicky the good boy is vicky')):
    print('search matches')
else:
    print('search not matches')

print(re.sub('vicky','vijay','vicky is a good boy'))


