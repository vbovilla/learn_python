# ask the user what acronym they want to add
acronym = input('What acronym do you want to add? \n')

# then ask the user for the definition
definition = input('What is the definition? \n')

# open the file
with open('./exceptions/acronyms_02.txt', 'a') as file:
    file.write(acronym+' - '+definition+'\n')
# write the new acronym and definition to the file
