
#Login file to control access when correct password entered.git
passwordFile = "Password@123"
secretPassword = passwordFile

typedPassword = input('Enteryour password: ')

if typedPassword == secretPassword:
    print('Access Granted')

elif typedPassword == '1234':
    print('This is not a lauggage bag')
    
else:
    print("Access Denied")