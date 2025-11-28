import os

# create directory 'cleanup' under 'exceptions'
try:
    os.mkdir('./exceptions/cleanup')
except FileExistsError as e:
    print('cleanup directory exists already')


# check if directory, 'cleanup' exists under 'exceptions'
dir_exists = os.path.exists('./exceptions/cleanup')
if dir_exists:
    print('cleanup directory exists under exceptions')

# check if the path provided is points to directory or file
is_file = os.path.isfile('./exceptions/cleanup')
if is_file:
    print('Path provided is a file')
else:
    print('Path provided is a directory')


is_dir = os.path.isdir('./exceptions/cleanup')
if not is_dir:
    print('Path provided is a file')
else:
    print('Path provided is a directory')


# Scan contents
entries = os.scandir('.')
for entry in entries:
    if os.path.isfile(entry):
        print('File: ', entry.name)
    elif os.path.isdir(entry):
        print('Directory: ', entry.name)
