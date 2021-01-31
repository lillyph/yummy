book = []

a = int(input('How many people would you like to be in your contact book?'))
for b in range(a):
    contact = []
    name = str(input('What is the name of your contact?'))
    phone = str(input('What is the phone number of your contact?'))
    contact.append(name)
    contact.append(phone)
    book.append(contact)

print('Your contact book is now complete! yeet')

answer = 'y'

while answer == 'y':
    choice = input('Choose a contact to refer to: ')


    for i in book:
        if i.count(choice) > 0:
            ind = i.index(choice)
            break


    if ind == 0:
        print(choice, 'was found.')
        print('Here is their contact information:')
        for elem in i:
            print(elem)

    answer = input('Would you like to see another contact? Enter y for yes and n for no: ')
        
