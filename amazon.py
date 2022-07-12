data = '''
                    MENU

        1) press 1 for add items
        2) press 2 for check items
        3) press 3 for remove items
        4) press 4 for view items


'''

amazone_store = []

print('Welcome to AMEZONE STORE')

status = True
while status:
    print(data)
    choice = int(input('enter your choice:'))
    if choice == 1:
        item_name = input('enter items:')
        amazone_store.append(item_name)
    elif choice == 2:
        item_name = input('enter item:')
        if item_name in amazone_store:
            print('AVILABLE')
        else:
            print('NOT AVILABLE')
    elif choice == 3:
        item_name = input('enter item:')
        if item_name in amazone_store:
            amazone_store.remove(item_name)
        else:
            print('sorry item not exists')
    elif choice == 4:
        print('total no. of item in amezone store: ',len(amazone_store))
        print('.............................')
        for item in amazone_store:
            print(item)
        print('......................')
    else:
        print('invalid input')
