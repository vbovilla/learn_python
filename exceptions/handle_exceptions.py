acronyms = {
    'LOL': 'laugh out loud',
    'IDK': "I don't know",
    'TBH': 'to be honest'
}

# try:
#     # try to read a key which is not available in the dictionary
#     definition = acronyms['BTW']
#     print(definition)
# except:
#     print('The key does not exist')

try:
    definition = acronyms['BTW']
except:
    print('The key does not exist')
finally:
    print('existing defintions:')
    for i in acronyms:
        print(i, '-->', acronyms[i])

print('print this after all')
