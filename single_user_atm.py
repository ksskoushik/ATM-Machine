username='ksskoushik'
password='2003'
pin=123
def homepage():
    print('welcome to pragati banking services')
    uname=str(input('enter username to login:'))
    if uname==username:
        upassword=str(input('enter password : '))
        if upassword==password:
            print('login successful')
            main()
        else:
            print('wrong password\ntry again')
            homepage()
    else:
        print('wrong username\ntry again')
        homepage()
def main():
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
                print('remaining balance:',balance)
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
                print('remaining balance is:',balance)
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
        oldpassword=str(input('enter old password : '))
        if password==oldpassword:
            newpassword=str(input('enter new password : '))
            newpasswordcheck=str(input('enter new password again : '))
            if newpassword==newpasswordcheck:
                password=newpassword
                print('password changed successfully')
                homepage()
            else: print('passwords does not match')
        else: print('wrong password try again')
    elif option==5:
        print('logout successful')
        homepage()
homepage()
