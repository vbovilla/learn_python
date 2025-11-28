# open the file
# file = open('acronyms.txt')
# with open('acronyms.txt') as file:

# file = open('./exceptions/acronyms.txt', 'r')
# try:
#     print('file name: ', file.name)
#     print('class name: ', file.__class__)
#     print('file mode: ', file.mode)
#     print('is file closed? ', file.closed)
#     print('buffer: ', file.buffer)
#     print('line buffering: ', file.line_buffering)
#     result = file.readlines()
#     for line in result:
#         print(line)
# except:
#     print('An exception occurred while opening and processing file')
# finally:
#     file.close()

# another way to read file
# with open('./exceptions/acronyms.txt', 'r') as file:
#     result = file.readlines()
#     for line in result:
#         print(line)


lookup = input('What acronym would you like to lookup? \n')

found = False
with open('./exceptions/acronyms.txt') as file:
    for line in file:
        if lookup in line:
            print(line)
            found = True
            break

if not found:
    print('The acronym does not exist in the file')
