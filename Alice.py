print('What is you name ? :')
myName = input()
if myName == 'Alice':
    print('Hi,Alice!')
else:
    print('What is your age ? :')
    myAge = input()
    if int(myAge)<12:
        print('You are not Alice.')
    elif int(myAge)>1000:
        print('You are not Alice,Alice not deaded')
    elif int(myAge)>100:
        print('You are not Alice, Alice not old.')
    else:
        print('You are neither Alice,nor little kid')
