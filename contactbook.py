contacts = []
hello = 1
print('Welcome to your contact book.\n What would you like to do?')
while hello = 1:
    choice = int(input('Enter 1: Add a new contact, 2: Delete a contact, 3: Adjust information of preexisting contact '))
    if choice == 1:
        name = input('What is the name of your new contact? ')
        number = input('What is their phone number? ')
        contacts.append(name)
        contacts.append(phone)
    elif: choice == 2:
        bye = input('Which contact would you like to delete? ')
        if bye in contacts:
            delete = contacts.index(bye)
            contacts[delete] = ''
            contacts[delete + 1] = ''
        else:
            print('That contact was not found in your contact book.')
    elif choice == 3:
        name = input('Which contact would you like to adjust?')
            if bye not in contacts:
                print('That contact was not found in your contact book.')
                continue
        location = contacts.index(name)
        haha = input('Enter 1: to adjust the name 2: to adjust the phone number ')
        if haha == 1
            new = input('You have chosen to change the name. What name would you like to change', contacts[location], 'contacts to?')



print(contacts)
    