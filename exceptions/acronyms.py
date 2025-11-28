
def find_acronym():
    acronym = input('Enter the acronym you want to find the definition for?\n')
    # open the file
    definition_found = False
    try:
        with open('./exceptions/acronyms_03.txt') as file:
            for line in file.readlines():
                if acronym in line:
                    definition_found = True
                    print('found the definition for acronym', acronym)
                    print(line)
                    break
    except FileNotFoundError as e:
        print('Acronyms file does not exist: Error message -> ', e)
        return

    if not definition_found:
        print(acronym, 'does not exists in the file')


def add_acronym():
    acronym = input('What acronym do you want to add? \n')
    definition = input('What is the definition? \n')
    with open('./exceptions/acronyms_01.txt', 'a') as file:
        file.write(acronym+' - '+definition+'\n')


def main():
    choice = input('Do you want find(F) or add(A) an acronym?\n')
    if choice == 'F':
        find_acronym()
    elif choice == 'A':
        add_acronym()


main()
