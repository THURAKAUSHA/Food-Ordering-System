print('1.Pizza')
print('2.Breadsticks')
print('3.Pasta')
print('4.Burger')
print('5.Cake')
print('6.Chips')
order=[]
ch='y'
while ch=='y':
    choice=int(input('Enter Your Item:'))
    if (choice>=1 and choice<=6):
        if choice==1:
             order.append('Pizza')
        elif choice==2:
             order.append('Breadsticks')
        elif choice==3:
             order.append('Pasta')
        elif choice==4:
             order.append('Burger')
        elif choice==5:
             order.append('Cake')
        else:
             order.append('Chips')
    else:
        print('invalid choice')
    ch=input('Do you want any item (y/n):')
print('Your order is:',order)
modify_order='y'
modify_order=input('Do you want to modify the Order(Y/N):')
if  modify_order=='y':
    print('1.Add an item')
    print('2.Delete an item')
    print('3.Modify an Item')
    choice2=int(input('Enter your choice:'))
    if choice2==1:
        print('1.Pizza')
        print('2.Breadsticks')
        print('3.Pasta')
        print('4.Burger')
        print('5.Cake')
        print('6.Chips')
        add='y'
        while add=='y':
            add1=int(input('Enter your choice:'))
            if (add1>=1 and add1<=6):
                if add1==1:
                    order.append('Pizza')
                elif add1==2:
                    order.append('Breadsticks')
                elif add1==3:
                    order.append('Pasta')
                elif add1==4:
                    order.append('Burger')
                elif add1==5:
                    order.append('Cake')
                else:
                    order.append('Pasta')
            else:
                print('invalid choice')
            add=input('Do you want to add any item (y/n):')
        print('Your order is:',order)
    elif choice2==2:
        remove=input('Enter an item to delete :')
        if remove in order:
            order.remove(remove)
        else:
            print('Sorry...! Item is not available')
        print('Your order is:',order)
    else:
        modify=input('Enter an item name to modify:')
        if modify in order:
            i=order.index(modify)
            m=input('Enter your New item:')
            order[i]=m
        else:
            print('Sorry...! Item is not available')
        print('Your order is :',order)
print('final oreder items are:',order)