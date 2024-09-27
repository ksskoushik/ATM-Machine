username=['koushik','ajay','afrid','bharat','balaji']
password=['ks','aj','af','bh','ba']
pin=['0000','1111','2222','3333','4444']
def loginpage():
    print('welcome to pragati banking services')
    request=int(input('new user ? enter 1 to register\nexisting user? enter 2 to login : '))
    if request==1:
        newuser()
    elif request==2:
        homepage()
def newuser():
    uname=str(int('enter new username : '))
    if uname in username:
            print('username already taken. choose another')
            newuser()
    print('your username is :',uname)
    newpassword()
    username.append(uname)
    password.append(upassword)
    pin.append(upin)
    
def newpassword():
    upassword=str(input('create new password : '))
    upasswordcheck=str(input('enter password again : '))
    if upassword==upasswordcheck:
        print('password created successfully')
        newpin()
    else:
        print('passwords miss match\ntry again')
        newpassword()
def newpin():
    upin=int(input('create new pin : '))
    upincheck=int(input('enter pin again : '))
    if upin==upincheck:
        print('pin created successfully')
        loginpage
    else: 
        print('pins miss match\ntry again')
        newpin()
    
def homepage():
    uname=str(input('enter username to login : '))
    if uname in username:
        index=username.index(uname)
        passwordcheck(index)
    else:
        print('wrong username\ntry again')
        homepage()
        
def passwordcheck(index):
        upassword=str(input('enter password : '))
        if upassword==password[index]:
            print('login successful')
            main(index)
        else:
            print('wrong password\ntry again')
            passwordcheck(index)
def main(index):
    print(' 1 withdraw 2 deposit\n 3 balance\n 4 change passsword\n 5 exit')
    option=int(input('enter number : '))
    balance=1000
    if option==1:
        amount=int(input('enter amount : '))
        if amount<=balance:
            balance=balance-amount
            print('transaction successful')
            balcheck=int(input('press 1 to check balance.\n press 2 to return to main menu'))
            if balcheck==1:
                print('remaining balance',balance)
            elif balcheck==2:
                main()
            else:
                print('invalid command')
                main()
        else: print('insufficient balance')
        main()
    elif option==2:
        amount=int(input('enter amount : '))
        balance=balance+amount
        print('transaction successful')
        balcheck=int(input('press 1 to check balance.\n press 2 to return to main menu : '))
        if balcheck==1:
                print('remaining balance is',balance)
        elif balcheck==0:
                main()
        else: print('invalid command')
        main()
    elif option==3:
        pinin=int(input('enter your pin number :'))
        if pinin==pin:
            print('verified.\nbalance amount is : ',balance)
        else: print('invalid.\ntry again')
        main()
    elif option==4:
        global password
        index=username.index(uname)
        oldpassword=str(input('enter old password : '))
        if password==oldpassword:
            newpassword=str(input('enter new password : '))
            newpasswordcheck=str(input('enter new password again : '))
            if newpassword==newpasswordcheck:
                password[index]=newpassword
                print('password changed successfully')
                homepage()
            else: print('passwords does not match')
        else: print('wrong password try again')
    elif option==5:
        print('logout successful')
        loginpage()
loginpage()
